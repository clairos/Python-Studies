from selenium import webdriver
from selenium.webdriver.chrome.service import Service # type: ignore
from selenium.webdriver.common.by import By # type: ignore
from selenium.webdriver.common.keys import Keys # type: ignore
from webdriver_manager.chrome import ChromeDriverManager # type: ignore
from selenium.webdriver.support.ui import WebDriverWait # type: ignore
from selenium.webdriver.support import expected_conditions as EC # type: ignore
from time import sleep
from urllib.parse import urlparse
from json import loads

# cria a instância do driver do navegador
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wdw = WebDriverWait(driver, 10)

url = 'https://curso-python-selenium.netlify.app/exercicio_04.html'

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

sleep(1)

divide_url = driver.current_url.split('?')
todos_atributos = divide_url[1]
todos_atributos = todos_atributos.split('&')
for atributo in todos_atributos:
    todos_atributos[atributo].split('=')
print(todos_atributos)
atributos_dic = {}


driver.quit()