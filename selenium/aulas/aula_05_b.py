from selenium import webdriver
from selenium.webdriver.chrome.service import Service # type: ignore
from selenium.webdriver.common.by import By # type: ignore
from selenium.webdriver.common.keys import Keys # type: ignore
from webdriver_manager.chrome import ChromeDriverManager # type: ignore
from selenium.webdriver.support.ui import WebDriverWait # type: ignore
from selenium.webdriver.support import expected_conditions as EC # type: ignore
from time import sleep

# cria a instância do driver do navegador
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wdw = WebDriverWait(driver, 10)

url = "https://curso-python-selenium.netlify.app/aula_05_b.html"

driver.get(url)

sleep(1)

topico = driver.find_element(By.CLASS_NAME, 'topico')
linguagens = driver.find_elements(By.CLASS_NAME, 'linguagens')

print(topico.text)

for linguagem in linguagens:
    print(linguagem.find_element(By.TAG_NAME, 'h2').text)

driver.quit()