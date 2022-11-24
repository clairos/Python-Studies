from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # type: ignore
from selenium.webdriver.common.by import By  # type: ignore

# from selenium.webdriver.common.keys import Keys  # type: ignore
from webdriver_manager.chrome import ChromeDriverManager  # type: ignore
from selenium.webdriver.support.ui import WebDriverWait  # type: ignore
from selenium.webdriver.support.events import AbstractEventListener  # type: ignore
from selenium.webdriver.support.events import EventFiringWebDriver  # type: ignore
from selenium.webdriver.support import expected_conditions as EC  # type: ignore
from time import sleep


class Escuta(AbstractEventListener):  # hook para pegar o que esta antes/depois
    def before_navigate_to(self, url, webdriver):
        print(f"Indo para {url}")

    def before_navigate_back(self, webdriver):
        print("voltando para a página anterior")

    def before_click(self, element, webdriver):
        if element.tag_name == "input":
            print(webdriver.find_element(By.TAG_NAME, "span").text)
        print(f"antes do click no {element.tag_name}")

    # def clicking(self, element, webdriver): # nao funciona
    #     print('to clicando')

    def after_click(self, element, webdriver):
        if element.tag_name == "input":
            print(webdriver.find_element(By.TAG_NAME, "span").text)
        print(f"depois do click no {element.tag_name}")


# cria a instância do driver do navegador
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wdw = WebDriverWait(driver, 10)

url = "https://curso-python-selenium.netlify.app/aula_07_d.html"

wrapper = EventFiringWebDriver(driver, Escuta())

wrapper.get(url)

sleep(1)

inp = wrapper.find_element(By.TAG_NAME, "input")
span = wrapper.find_element(By.TAG_NAME, "span")
p = wrapper.find_element(By.TAG_NAME, "p")

inp.click()
span.click()
# print('to clicando')

new_url = "https://curso-python-selenium.netlify.app/aula_07_c.html"

wrapper.get(new_url)

wrapper.back()

driver.quit()
