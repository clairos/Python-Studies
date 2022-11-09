from selenium import webdriver
from selenium.webdriver.chrome.service import Service # type: ignore
from selenium.webdriver.common.by import By # type: ignore
from selenium.webdriver.common.keys import Keys # type: ignore
from webdriver_manager.chrome import ChromeDriverManager # type: ignore
from selenium.webdriver.support.ui import WebDriverWait # type: ignore
from selenium.webdriver.support import expected_conditions as EC # type: ignore
from time import sleep
from pprint import pprint # pretty print

# retorna um dicionario com os link das tags 'a' dentro de outra tag (ex. 'main')
def get_link(driver, elemento): 
    result = {}

    element = driver.find_element(By.TAG_NAME, elemento)
    ancoras = element.find_elements(By.TAG_NAME, 'a')

    for ancora in ancoras:
        result[ancora.text] = ancora.get_attribute('href')
    
    return result

# retorna elemento que tenha o link especifico no atributo 'href'
def find_c_e(driver, link):
    elementos = driver.find_elements(By.TAG_NAME, 'a')

    for elemento in elementos:
        if link in elemento.get_attribute('href'):
            return elemento

# cria a instância do driver do navegador
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wdw = WebDriverWait(driver, 10)

url = "https://curso-python-selenium.netlify.app/exercicio_03.html"

#entra na URL do exercicio 3
driver.get(url)
sleep(1)

#começa o exercício
start = get_link(driver, 'main')
driver.get(start['Começar por aqui'])

# pagina 1
sleep(0.8)
errado = find_c_e(driver, 'page_2')
click_e = errado.get_attribute('href')
driver.get(click_e)

# pagina 2
sleep(0.8)
certo = find_c_e(driver, 'page_3')
click_c = certo.get_attribute('href')
driver.get(click_c)

# pagina 3
sleep(0.8)
certo = find_c_e(driver, 'page_4')
click_c = certo.get_attribute('href')
driver.get(click_c)

# pagina 4
sleep(0.8)
driver.refresh()

# fim do jogo!
sleep(0.8)

driver.quit()