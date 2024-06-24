from flask import Blueprint, request,jsonify
from model.config import ConfigScrap
from core.scraper import getExecutor
import json

search = Blueprint('search', __name__)

@search.route('/search', methods=['POST'])
def search_route():
    search_type = request.form.get('type', 'linkedin')
    keyword = request.form.get('keyword', '')
    location = request.form.get('location', 'Leon, Guanajuato')
    initial_page = int(request.form.get('initial_page', 1))
    final_page = int(request.form.get('final_page', 1))
    profiles_to_search = request.form.get('profiles_to_search', '[]')
    is_search = request.form.get('is_search', 'false').lower() == 'true'

    # Convert profiles_to_search to a list using json.loads for safety
    profiles_to_search = json.loads(profiles_to_search)

    conf = ConfigScrap(keyword=keyword, location=location, initial_page=initial_page, final_page=final_page,
                       profiles_to_search=profiles_to_search, is_search=is_search, type=search_type)
    
    print(f"ConfigScrap: {conf}")
    print(f"Type of profiles_to_search: {type(conf.profiles_to_search)}")
    
    #convertir conf.profiles_to_search a lista si es un string ese se ve como "['profile1','profile2']"
    if isinstance(conf.profiles_to_search, str):
        conf.profiles_to_search = conf.profiles_to_search.replace("[","").replace("]","").replace("'","").split(",")

    #imprimir el tipo de profiles_to_search
    print(f"Type of profiles_to_search: {type(conf.profiles_to_search)}")

    executor = getExecutor(conf.type)
    
    print(f"is correct executor: {executor.is_ok}")

    if executor.is_ok:
        result = executor.value.execute(conf)
        if result:
            return {
                "status": "ok",
                "data": result
            }
    else:
        return {
            "status": "error",
            "message": "Invalid executor type"
        }
    
    return {
        "status": "error",
        "message": "An error occurred"
    }

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import pickle
import os

def getExperienceData(driver):
    soup = BeautifulSoup(driver.page_source, 'lxml')
    sections = soup.find_all('div', id='experience')
    if not sections:
        return None
    # Sections next sibling
    next_sibling = sections[0].find_next_sibling()
    # Second next sibling
    second_next_sibling = next_sibling.find_next_sibling()
    experiencias = []
    sections = second_next_sibling.find_all('li', class_='artdeco-list__item')
    for section in sections:
        duracion = section.find('span', class_='t-14 t-normal t-black--light').get_text(strip=True)
        empresa = section.find('span', class_='t-14 t-normal').get_text(strip=True)
        cargo = section.find('div', class_='display-flex align-items-center mr1 t-bold').get_text(strip=True)
        actividades = section.find('div', class_='FKFqOBZeKsYhiuZKTYcfkNJIpRwfptzrAEOM').get_text(strip=True)
        experiencias.append({
            'duración': duracion,
            'empresa': empresa,
            'cargo': cargo,
            'actividades': actividades
        })
    return experiencias


def getEducationData(driver):
    soup = BeautifulSoup(driver.page_source, 'lxml')
    sections = soup.find_all('div', id='education')
    if not sections:
        return None
    # Sections next sibling
    next_sibling = sections[0].find_next_sibling()
    # Second next sibling
    second_next_sibling = next_sibling.find_next_sibling()
    educaciones = []
    sections = second_next_sibling.find_all('li', class_='artdeco-list__item')
    for section in sections:
        duracion = section.find('span', class_='pvs-entity__caption-wrapper').get_text(strip=True) if section.find('span', class_='pvs-entity__caption-wrapper') else "No hay duración"
        carrera = section.find('span', class_='t-14 t-normal').get_text(strip=True) if section.find('span', class_='t-14 t-normal') else "No hay escuela"
        escuela = section.find('div', class_='display-flex align-items-center mr1 t-bold').text.strip() if section.find('div', class_='display-flex align-items-center mr1 t-bold') else "No hay carrera"
        educaciones.append({
            'duración': duracion,
            'escuela': escuela,
            'carrera': carrera
        })
    return educaciones


def getLicencias_certificacionesData(driver):
    soup = BeautifulSoup(driver.page_source, 'lxml')
    sections = soup.find_all('div', id='licenses_and_certifications')
    if not sections:
        return None
    # Sections next sibling
    next_sibling = sections[0].find_next_sibling()
    # Second next sibling
    second_next_sibling = next_sibling.find_next_sibling()
    licencias_certificaciones = []
    sections = second_next_sibling.find_all('li', class_='artdeco-list__item')
    for section in sections:
        img = section.find('img')['src'] if section.find('img') else "No hay imagen"
        nombre = section.find('div', class_='display-flex align-items-center mr1 hoverable-link-text t-bold').get_text(strip=True) if section.find('div', class_='display-flex align-items-center mr1 hoverable-link-text t-bold') else "No hay nombre"
        plataforma = section.find('span', class_='t-14 t-normal').get_text(strip=True) if section.find('span', class_='t-14 t-normal') else "No hay plataforma"
        expedicion = section.find('span', class_='t-14 t-normal t-black--light').get_text(strip=True) if section.find('span', class_='t-14 t-normal t-black--light') else "No hay expedicion"
        URL_certificacion = section.find('a')['href'] if section.find('a') else "No hay URL"
        licencias_certificaciones.append({
            'img': img,
            'nombre': nombre,
            'plataforma': plataforma,
            'expedicion': expedicion,
            'URL_certificacion': URL_certificacion
        })
    return licencias_certificaciones


@search.route('/searcht', methods=['POST'])
def test():
    # Configuración de opciones para el navegador
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-gpu')
    data = '/home/ubuntu/demo/CHROMEDRIVER'
    options.add_argument("--user-data-dir=" + data)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    # Navegar al perfil de Daniel Ruiz
    driver.get("https://www.linkedin.com/in/daniel-ruiz-guti%C3%A9rrez-3a925b65/")

    id_needed_login = "public_profile_contextual-sign-in_sign-in-modal"

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, id_needed_login
        )))
        return jsonify({
            "status": "error",
            "message": "Login needed"
        })

    except Exception as e:
        pass
        



    certificaciones = getLicencias_certificacionesData(driver)

    driver.quit()

    return jsonify({
        "status": "ok",
        "data": {
            "certificaciones": certificaciones if certificaciones else []
        }
    })

@search.route('/login', methods=['POST'])
def login():
    # Configuración de opciones para el navegador
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-gpu')
    data = '/home/ubuntu/demo/CHROMEDRIVER'
    options.add_argument("--user-data-dir=" + data)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Iniciar sesión en LinkedIn
    driver.get("https://www.linkedin.com/login")

    if "feed" in driver.current_url:
        driver.quit()
        return jsonify({
            "status": "ok",
            "message": "Already logged in"
        })

    user = "meta.dev@forteinnovation.mx"
    password = "m3t4.dev-321"


    username = driver.find_element(By.ID, "username")
    username.send_keys(user)

    pword = driver.find_element(By.ID, "password")
    pword.send_keys(password)

    driver.find_element(By.XPATH, "/html/body/div/main/div[2]/div[1]/form/div[3]/button").click()

    # Esperar a que la página se cargue completamente después de intentar iniciar sesión
    time.sleep(3)

    # Comprobar si el login fue exitoso
    if "feed" in driver.current_url:
        driver.quit()
        return jsonify({
            "status": "ok",
            "message": "Login successful"
        })

    # Capturar mensaje de error
    error_message = None
    try:
        error_element = driver.find_element(By.XPATH, "//div[@role='alert']")
        error_message = error_element.text
    except Exception as e:
        error_message = "No error message found"

    source = driver.page_source
    driver.quit()
    return jsonify({
        "status": "error",
        "message": "Login failed",
        "error_message": error_message,
        "url": driver.current_url,
        "response": source
    })









