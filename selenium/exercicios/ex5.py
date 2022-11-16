from selenium import webdriver
from selenium.webdriver.chrome.service import Service # type: ignore
from selenium.webdriver.common.by import By # type: ignore
from selenium.webdriver.common.keys import Keys # type: ignore
from webdriver_manager.chrome import ChromeDriverManager # type: ignore
from selenium.webdriver.support.ui import WebDriverWait # type: ignore
from selenium.webdriver.support import expected_conditions as EC # type: ignore
from time import sleep
from urllib.parse import urlparse

# cria a instância do driver do navegador
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wdw = WebDriverWait(driver, 10)

url = 'https://curso-python-selenium.netlify.app/exercicio_05.html'

driver.get(url)

sleep(1)

nomes = driver.find_elements(By.CSS_SELECTOR, '[type=text]')
senhas = driver.find_elements(By.CSS_SELECTOR, '[type=password]')
btns = driver.find_elements(By.CSS_SELECTOR, 'input[name*=l]')

for nome in nomes:
    nome.send_keys('Clara')

for senha in senhas:
    senha.send_keys('submarino123')

for btn in btns:
    btn.click()
    sleep(1)

sleep(2)

driver.quit()