from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # type: ignore
from selenium.webdriver.common.by import By  # type: ignore
from selenium.webdriver.common.keys import Keys  # type: ignore
from webdriver_manager.chrome import ChromeDriverManager  # type: ignore
from selenium.webdriver.support.ui import WebDriverWait  # type: ignore
from selenium.webdriver.support import expected_conditions as EC  # type: ignore
from time import sleep
from urllib.parse import urlparse
from json import loads

# cria a instância do driver do navegador
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wdw = WebDriverWait(driver, 10)

url = 'https://curso-python-selenium.netlify.app/aula_05.html'

def preenche_form(browser, nome, email, senha, telefone):
    browser.find_element(By.NAME, 'nome').send_keys(nome)
    browser.find_element(By.NAME, 'email').send_keys(email)
    browser.find_element(By.NAME, 'senha').send_keys(senha)
    browser.find_element(By.NAME, 'telefone').send_keys(telefone)
    browser.find_element(By.NAME, 'btn').click()

driver.get(url)

sleep(1)

estrutura = {
    'nome': 'Clara',
    'email': 'clara@gmail.com',
    'senha': 'senha1234',
    'telefone': '49999024915'
}

preenche_form(driver, **estrutura)

# print(urlparse(driver.current_url))
sleep(1)

texto_result = driver.find_element(By.ID, 'result').text
result_arrumado = texto_result.replace('\'', '\"')

dic_result = loads(result_arrumado)

if dic_result==estrutura:
    print('deu certo!')
else:
    print('não deu certo :(')

driver.quit()
