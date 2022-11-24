from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # type: ignore
from selenium.webdriver.common.by import By  # type: ignore
# from selenium.webdriver.common.keys import Keys  # type: ignore
from webdriver_manager.chrome import ChromeDriverManager  # type: ignore
from selenium.webdriver.support.ui import WebDriverWait  # type: ignore
from selenium.webdriver.support.events import AbstractEventListener, EventFiringWebDriver # type: ignore
from selenium.webdriver.support import expected_conditions as EC  # type: ignore
from time import sleep

class Escuta(AbstractEventListener):
    def before_click(self, element, webdriver):
        if element.tag_name == 'input':
            print(webdriver.find_element(By.TAG_NAME, 'span').text)
        print(f'antes do click no {element.tag_name}')

    # def clicking(self, element, webdriver):
    #     print('to clicando')

    def after_click(self, element, webdriver):
        if element.tag_name == 'input':
            print(webdriver.find_element(By.TAG_NAME, 'span').text)
        print(f'depois do click no {element.tag_name}')	

# cria a instância do driver do navegador
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wdw = WebDriverWait(driver, 10)

url = 'https://curso-python-selenium.netlify.app/aula_07_d.html'

rap10 = EventFiringWebDriver(driver, Escuta())

rap10.get(url)

sleep(1)

inp = rap10.find_element(By.TAG_NAME, 'input')
span = rap10.find_element(By.TAG_NAME, 'span')
p = rap10.find_element(By.TAG_NAME, 'p')

inp.click()
span.click()
# print('to clicando')

driver.quit()