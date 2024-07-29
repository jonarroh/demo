import os
import time
from typing import List

import pandas as pd
from bs4 import BeautifulSoup
from pandas import DataFrame
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def getOffer(urls: List[str], driver):
    try:
        search = urls[0]

        print(f"Buscando ofertas en {search}")

        driver.get(search)
        time.sleep(10)

        src = driver.page_source
        
        with open("source.html", "w") as file:
            file.write(src)

        soup = BeautifulSoup(src, 'lxml')

        offers = soup.find('ul', {'class': 'jobs-search__results-list'})

        if offers is None:
            print("No se encontraron ofertas.")
            return pd.DataFrame()

        results = []

        for offer in offers.find_all('li'):
            title_elem = offer.find('h3', {'class': 'base-search-card__title'})
            title = title_elem.text.strip() if title_elem else 'N/A'

            company_elem = offer.find('h4', {'class': 'base-search-card__subtitle'})
            company = company_elem.text.strip() if company_elem else 'N/A'

            location_elem = offer.find('span', {'class': 'job-search-card__location'})
            location = location_elem.text.strip() if location_elem else 'N/A'

            date_elem = offer.find('time', {'class': 'job-search-card__listdate'})
            date = date_elem.text.strip() if date_elem else 'N/A'

            url_elem = offer.find('a', {'class': 'base-card__full-link'})
            url = url_elem['href'] if url_elem else 'N/A'

            results.append([title, company, location, date, url])

        for index, result in enumerate(results):
            #liminar a 30 ofertas
            if index == 5:
                break

            print(f"Obteniendo criterios de la oferta {index + 1} de {len(results)}")
            criteria = get_criteria(driver, result[4])
            results[index].append(criteria)

        return pd.DataFrame(results, columns=['title', 'company', 'location', 'date', 'url', 'criteria'])
    except Exception as e:
        print(e)
        return pd.DataFrame()

def get_criteria(driver, url):
    driver.get(url)
    time.sleep(2)
    src = driver.page_source
    soup = BeautifulSoup(src, 'lxml')
    
    # Encontrar el ul con description__job-criteria-list
    ul = soup.find('ul', class_='description__job-criteria-list')
    
    # Iterar sobre cada li en el ul y obtener los valores
    criteria = {'url': url}
    if ul:
        for li in ul.find_all('li', class_='description__job-criteria-item'):
            header = li.find('h3', class_='description__job-criteria-subheader').get_text(strip=True)
            value = li.find('span', class_='description__job-criteria-text').get_text(strip=True)
            criteria[header] = value

    return criteria

class Scraper:
    def search_jobs(config) -> DataFrame:
        keyword = config.keyword
        location = config.location

        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--disable-extensions')
        options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        search_url = "https://www.google.com"
        driver.get(search_url)

        # Esperar hasta que el campo de entrada de búsqueda esté presente en la página
        input_search = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "q")))

        input_search.send_keys(f"site:linkedin.com/jobs {keyword} {location}")
        input_search.submit()

        for _ in range(1):
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "rcnt")))

            src = driver.page_source

            soup = BeautifulSoup(src, 'lxml')
            profiles = soup.find_all('div', class_='MjjYud')

            urls_profiles = []

            for profile in profiles:
                link_tag = profile.find('a')
                if link_tag is not None:
                    profile_linkedin_url = link_tag['href']
                    try:
                        if profile_linkedin_url.startswith('/search'):
                            break
                        urls_profiles.append(profile_linkedin_url)
                    except Exception as e:
                        print(e)
                        print(f"Error en {profile_linkedin_url}")
                else:
                    print("No se encontró una etiqueta <a> en este perfil:", profile)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        print("Se encontraron", len(urls_profiles), "perfiles")
        return getOffer(urls_profiles, driver)
