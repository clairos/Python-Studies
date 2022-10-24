from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def find_by_text(driver, tag, texto):
    elementos = driver.find_elements(By.TAG_NAME, tag) # lista

    for elemento in elementos:
        if elemento.text == texto:
            return elemento

# cria a instância do driver do navegador
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wdw = WebDriverWait(driver, 10)

url = "https://selenium.dunossauro.live/aula_04_b.html"

driver.get(url)

sleep(1)

nomes_das_caixas = ['um', 'dois', 'tres', 'quatro']

for nome in nomes_das_caixas:
    sleep(0.3)
    find_by_text(driver, 'div', nome).click()

# sleep(1)

for nome in nomes_das_caixas:
    sleep(0.3)
    driver.back()

for nome in nomes_das_caixas:
    sleep(0.3)
    driver.forward()

sleep(0.5)

driver.quit()