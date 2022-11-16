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

def preencheForm(form, nome, senha):
    driver.find_element(By.CSS_SELECTOR, f'form.form-{form} [name="nome"]').send_keys(nome)
    driver.find_element(By.CSS_SELECTOR, f'form.form-{form} [name="senha"]').send_keys(senha)
    driver.find_element(By.CSS_SELECTOR, f" form.form-{form} [name={form}]").click()

for i in range(4):
    nform = driver.find_element(By.CSS_SELECTOR, 'header span')
    preencheForm(nform.text, 'clara', 'senhateste123')
    sleep(0.5)

sleep(1)

driver.quit()