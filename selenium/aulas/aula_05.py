from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # type: ignore
from selenium.webdriver.common.by import By  # type: ignore
from selenium.webdriver.common.keys import Keys  # type: ignore
from webdriver_manager.chrome import ChromeDriverManager  # type: ignore
from selenium.webdriver.support.ui import WebDriverWait  # type: ignore
from selenium.webdriver.support import expected_conditions as EC  # type: ignore
from time import sleep

# cria a instância do driver do navegador
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wdw = WebDriverWait(driver, 10)

url = "https://curso-python-selenium.netlify.app/aula_05.html"

def preenche_form(browser, nome, email, senha, telefone):
    browser.find_element(By.NAME, "nome").send_keys(nome)
    browser.find_element(By.NAME, "email").send_keys(email)
    browser.find_element(By.NAME, "senha").send_keys(senha)
    browser.find_element(By.NAME, "telefone").send_keys(telefone)
    browser.find_element(By.NAME, "btn").click()

driver.get(url)

sleep(1)

preenche_form(driver, "Clara", "clarasgore@gmail.com", "senha1234", "49999024915")

# sleep(3)

driver.quit()
