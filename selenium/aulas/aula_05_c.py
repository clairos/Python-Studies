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

url = "https://curso-python-selenium.netlify.app/aula_05_c.html"

driver.get(url)

sleep(1)

def melhor_filme(browser, filme, email, telefone):
    browser.find_element(By.NAME, 'filme').send_keys(filme)
    browser.find_element(By.NAME, 'email').send_keys(email)
    browser.find_element(By.NAME, 'telefone').send_keys(telefone)
    browser.find_element(By.NAME, 'enviar').click()

# driver.find_element(By.NAME, 'filme').send_keys('Bacurau')
# email = driver.find_element(By.NAME, 'email')
# email.send_keys('email@gmail.com')
# driver.find_element(By.NAME, 'telefone').send_keys('(049)999024915')
# botao = driver.find_element(By.NAME, 'enviar')
# botao.click()

melhor_filme(driver, 'Bacurau', 'clarasgore@gmail.com', '(049)999024915')

driver.quit()