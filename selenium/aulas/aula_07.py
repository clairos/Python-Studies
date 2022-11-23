from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # type: ignore
from selenium.webdriver.common.by import By  # type: ignore
# from selenium.webdriver.common.keys import Keys  # type: ignore
from webdriver_manager.chrome import ChromeDriverManager  # type: ignore
from selenium.webdriver.support.ui import WebDriverWait  # type: ignore
from selenium.webdriver.support.events import AbstractEventListener # type: ignore
from selenium.webdriver.support import expected_conditions as EC  # type: ignore
from time import sleep

class Escuta(AbstractEventListener):
    def before_click(self, element, webdriver):
        print('antes do click')

    def after_click(self, element, webdriver):
        print('depois do click')

# cria a instância do driver do navegador
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wdw = WebDriverWait(driver, 10)

url = 'https://curso-python-selenium.netlify.app/aula_07_d.html'

driver.get(url)

sleep(1)

inp = driver.find_element(By.TAG_NAME, 'input')
span = driver.find_element(By.TAG_NAME, 'span')
p = driver.find_element(By.TAG_NAME, 'p')

inp.click()
print('to clicando')

driver.quit()