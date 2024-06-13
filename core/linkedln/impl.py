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
from utils.const import *


def init_cli():
    mjs = """
    _________.__              .__  .__  __  .__        ___________.__
    ____________________  _____       _____  __________________________   
    \______   \______   \/  _  \     /     \ \_   _____|__    ___/  _  \  
     |       _/|     ___/  /_\  \   /  \ /  \ |    __)_  |    | /  /_\  \ 
     |    |   \|    |  /    |    \ /    Y    \|        \ |    |/    |    \\
     |____|_  /|____|  \____|__  / \____|__  /_______  / |____|\____|__  /
            \/                 \/          \/        \/                \/ 
   """
    print(mjs)

def get_one_profile(driver,curren_url: str):
    # obtener el codigo de la pagina
    src = driver.page_source
    soup = BeautifulSoup(src, 'lxml')
    #Obtener el ur de la imagen
    div = soup.find('div', class_='pv-top-card__non-self-photo-wrapper ml0')
    img = div.find('img')['src'] if div else "No hay imagen"

    

    nombre = soup.find('h1', class_='text-heading-xlarge inline t-24 v-align-middle break-words')
    print(f"el nombre es: {nombre}")
    nombre = nombre.text.strip() if nombre else "No hay nombre"
    description = soup.find('div', class_= 'text-body-medium break-words')
    description = description.text.strip() if description else "No hay descripcion"
    empresa_actual = soup.find('div', class_='inline-show-more-text inline-show-more-text--is-collapsed inline-show-more-text--is-collapsed-with-line-clamp inline')
    empresa_actual = empresa_actual.text.strip() if empresa_actual else "No hay empresa actual"
    about = soup.find('section', class_='artdeco-card ember-view relative break-words pb3 mt2')
    if about:
      about = about.find('div', class_='inline-show-more-text inline-show-more-text--is-collapsed inline-show-more-text--is-collapsed-with-line-clamp full-width')
      about = about.text.strip() if about else "No hay about"
      about = about.replace("… ver más", "")
    
    
    conocimientos_aptitudes = soup.find_all('div', class_='pvs-entity pvs-entity--padded pvs-list__item--no-padding-in-columns')
    conocimiento = [{
      "nombre": conocimiento_aptitud.find('div', class_='display-flex align-items-center mr1 hoverable-link-text t-bold').text.strip() if conocimiento_aptitud.find('div', class_='display-flex align-items-center mr1 hoverable-link-text t-bold') else "No hay nombre",
      "descripcion": conocimiento_aptitud.find('div', class_='inline-show-more-text inline-show-more-text--is-collapsed inline-show-more-text--is-collapsed-with-line-clamp full-width').text.strip() if conocimiento_aptitud.find('div', class_='inline-show-more-text inline-show-more-text--is-collapsed inline-show-more-text--is-collapsed-with-line-clamp full-width') else "No hay descripcion",
    }
    for conocimiento_aptitud in conocimientos_aptitudes
    ]
    info_idiomas = soup.find_all('section', class_='artdeco-card ember-view relative break-words pb3 mt2')
    info_idiomas = [idioma for idioma in info_idiomas if idioma.find('div', id='languages')]
    idiomas = []
    for idioma in info_idiomas:
        items = idioma.find_all('li', class_='artdeco-list__item pvs-list__item--line-separated pvs-list__item--one-column')
        for item in items:
            nombre_idioma = item.find('div', class_='display-flex align-items-center mr1 t-bold').text.strip() if item.find('div', class_='display-flex align-items-center mr1 t-bold') else "No hay idioma"
            nivel = item.find('span', class_='t-14 t-normal t-black--light').text.strip() if item.find('span', class_='t-14 t-normal t-black--light') else "No hay nivel"
            idioma_data = {
                "idioma": nombre_idioma,
                "nivel": nivel
            }
            idiomas.append(idioma_data)
    educaciones = soup.find_all('section', class_='artdeco-card ember-view relative break-words pb3 mt2')
    educaciones = [edu for edu in educaciones if edu.find('div', id='education')]
    educacion = []
    for edu in educaciones:
        items = edu.find_all('li', class_='artdeco-list__item pvs-list__item--line-separated pvs-list__item--one-column')
        for item in items:
            img = item.find('img')['src'] if item.find('img') else "No hay imagen"
            escuela = item.find('div', class_='display-flex align-items-center mr1 hoverable-link-text t-bold').text.strip() if item.find('div', class_='display-flex align-items-center mr1 hoverable-link-text t-bold') else "No hay nombre"
            especialidad = item.find('span', class_='t-14 t-normal').text.strip() if item.find('span', class_='pv-entity__secondary-title pv-entity__fos t-14 t-black t-normal') else "No hay especialidad"
            educacion_data = {
                "img": img,
                "escuela": escuela,
                "especialidad": especialidad
            }
            
            educacion.append(educacion_data)
  
    licencias_certificaciones = soup.find_all('section', class_='artdeco-card ember-view relative break-words pb3 mt2')
    licencias = []
    for licencia in licencias_certificaciones:
        if licencia.find('div', id='licenses_and_certifications'):
            items = licencia.find_all('li', class_='artdeco-list__item pvs-list__item--line-separated pvs-list__item--one-column')
            for item in items:
                img = item.find('img')['src'] if item.find('img') else "No hay imagen"
                nombre = item.find('div', class_='display-flex align-items-center mr1 hoverable-link-text t-bold').text.strip() if item.find('div', class_='display-flex align-items-center mr1 hoverable-link-text t-bold') else "No hay nombre"
                plataforma = item.find('span', class_='t-14 t-normal').text.strip() if item.find('span', class_='t-14 t-normal') else "No hay plataforma"
                expedicion = item.find('span', class_='t-14 t-normal t-black--light').text.strip() if item.find('span', class_='t-14 t-normal t-black--light') else "No hay expedicion"
                URL_certificacion = item.find('a')['href'] if item.find('a') else "No hay URL"
                licencia_data = {
                    "img": img,
                    "nombre": nombre,
                    "plataforma": plataforma,
                    "expedicion": expedicion,
                    "URL_certificacion": URL_certificacion
                }
                licencias.append(licencia_data)
    info = {
       "url": curren_url,
        "nombre": nombre,
        "img": img,
        "description": description,
        "empresa_actual": empresa_actual,
        "about": about if about else "No hay about",
        "idiomas": idiomas if idiomas else "No hay idiomas",
        "conocimientos_aptitudes" : conocimiento if conocimiento else "No hay conocimientos y aptitudes",
        "educacion": educacion if educacion else "No hay educacion",
        "licencias_certificaciones": licencias if licencias else "No hay licencias y certificaciones"
    }
    return info

def scrap_data_from_profile(driver,urls_profiles: List[str]):
  print("Extrayendo datos de los perfiles" + str(urls_profiles))
  data_profiles = []
  for url in urls_profiles:
      driver.get(url)
      #imprimir el html de la pagina

      print(f"Extrayendo datos de {url}")
      print(driver.page_source)
      #mandar el html a un archivo
      with open('profile.html', 'w') as file:
        file.write(driver.page_source)
        

      try:
         WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'application-outlet')))
      except Exception as e:
        print(e)
        print(f"Error en {url}")
        time.sleep(5)
        continue
      #ir hasta abajo de la pagina
      driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
      time.sleep(5)
      #obtener la informacion del perfil
      print("Obteniendo la informacion del perfil")
      data_profiles.append(get_one_profile(driver,url))
  return data_profiles

def search_by_keyword(driver, config, urls_profiles: List[str]):
    keywords = config.keyword
    location = config.location
    initial_page = int(config.initial_page)
    final_page = int(config.final_page)


    print(f"Buscando perfiles de {keywords} en {location} desde la página {initial_page} hasta la página {final_page}")
    
    # Abrir la página de búsqueda
    search_url = "https://www.google.com"
    driver.get(search_url)

    # Esperar hasta que el campo de entrada de búsqueda esté presente en la página
    input_search = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "q")))

    input_search.send_keys(f"site:linkedin.com/in/ AND {keywords} AND {location}")
    input_search.submit()

    for _ in range(initial_page, final_page + 1):
        # Esperar hasta que aparezca el elemento de resultados de búsqueda en la página
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'rcnt')))

        # Obtener el código fuente de la página de resultados de búsqueda
        src = driver.page_source

        # Pasear el HTML
        soup = BeautifulSoup(src, 'lxml')
        profiles = soup.find_all('div', class_='MjjYud')
        
        for profile in profiles:
            link_tag = profile.find('a')
            if link_tag is not None:  # Verificar si link_tag no es None
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
        
        # Saber si hay botón de siguiente o scroll infinito
        try:
            next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'pnnext')))
            next_button.click()
        except Exception as e:
            print(e)
            break
    
    print(f"Se encontraron {len(urls_profiles)} perfiles")
    print(urls_profiles)

    info = scrap_data_from_profile(driver, urls_profiles)
    df = pd.DataFrame(info)
    return df

def search_by_urls(driver,urls_profiles: List[str]):
    info = scrap_data_from_profile(driver, urls_profiles)
    print(info)
    df = pd.DataFrame(info)

    return df


from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class Scraper:  
    def search_people(config) -> DataFrame:
      init_cli()
      
      is_search:bool = config.is_search
      profiles_to_search:List[str] = config.profiles_to_search
      urls_profiles = []
      df:DataFrame = pd.DataFrame()

      options = Options()
      options.add_argument('--headless')
      options.add_argument('--no-sandbox')
      options.add_argument('--disable-dev-shm-usage')
      driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

      print(f"launching {LOGIN_URL}")
      # Logging into LinkedIn
      driver.get("https://www.linkedin.com/login")

      #mandar el html a un archivo
      with open('login.html', 'w') as file:
        file.write(driver.page_source)



      time.sleep(4)

      user = os.getenv("LINKEDIN_USER")
      password = os.getenv("LINKEDIN_PASSWORD")

      print(f"Logging in with {user} and {password}")

      username = driver.find_element(By.ID, "username")
      username.send_keys(user)

      pword = driver.find_element(By.ID, "password")
      pword.send_keys(password)

      #encontrar el boton de login con el aria-label de "Sign in"
      login_button = driver.find_element(By.XPATH, "//button[@aria-label='Sign in']")

      login_button.click()

      time.sleep(4)

      print(f"is_search: {is_search}")
      if is_search:
        print("Buscando por urls")
        df = search_by_urls(driver,profiles_to_search)
      else:
        df = search_by_keyword(driver,config,urls_profiles)
      driver.quit()
      return df
