from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from pprint import pprint # pretty print

# cria a instância do driver do navegador
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wdw = WebDriverWait(driver, 10)

url = "https://curso-python-selenium.netlify.app/aula_04.html"

driver.get(url)

sleep(1)

def get_links(driver, elemento):
    result = {}
    element = driver.find_element(By.TAG_NAME, elemento)
    ancoras = element.find_elements(By.TAG_NAME, 'a')

    for ancora in ancoras:
        result[ancora.text] = ancora.get_attribute('href')

    return result

aulas = get_links(driver, 'aside')
pprint(aulas)

exercicios = get_links(driver, 'main')
pprint(exercicios)

driver.get(exercicios['Exercício 3'])

# sleep(2)

# driver.back()

# sleep(1)

driver.quit()