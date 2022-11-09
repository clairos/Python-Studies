# aninhada

from selenium import webdriver
from selenium.webdriver.chrome.service import Service # type: ignore
from selenium.webdriver.common.by import By # type: ignore
from selenium.webdriver.common.keys import Keys # type: ignore
from webdriver_manager.chrome import ChromeDriverManager # type: ignore
from selenium.webdriver.support.ui import WebDriverWait # type: ignore
from selenium.webdriver.support import expected_conditions as EC # type: ignore
from time import sleep

def find_by_text(driver, tag, texto):
    elementos = driver.find_elements(By.TAG_NAME, tag) # lista

    for elemento in elementos:
        if elemento.text == texto:
            return elemento

def find_by_href(driver, link):
    elementos = driver.find_elements(By.TAG_NAME, 'a')

    for elemento in elementos:
        if link in elemento.get_attribute('href'):
            return elemento

# cria a instância do driver do navegador
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wdw = WebDriverWait(driver, 10)

url = "https://selenium.dunossauro.live/aula_04_a.html"

driver.get(url)

sleep(1)

elemento_ddg = find_by_text(driver, 'a', 'DuckDuckGo')
print(elemento_ddg.text)
print(elemento_ddg.get_attribute('href'))

elemento_g = find_by_href(driver, 'google')
print(elemento_g.get_attribute('href'))

driver.quit()