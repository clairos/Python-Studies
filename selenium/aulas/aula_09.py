from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # type: ignore
from selenium.webdriver.common.by import By  # type: ignore
from selenium.webdriver.common.keys import Keys  # type: ignore
from selenium.webdriver.common.action_chains import ActionChains # type: ignore
from webdriver_manager.chrome import ChromeDriverManager  # type: ignore
from selenium.webdriver.support.ui import WebDriverWait  # type: ignore
from selenium.webdriver.support.events import AbstractEventListener  # type: ignore
from selenium.webdriver.support.events import EventFiringWebDriver  # type: ignore
from selenium.webdriver.support import expected_conditions as EC  # type: ignore

# cria a instância do driver do navegador
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wdw = WebDriverWait(driver, 10)

url = "https://selenium.dunossauro.live/aula_09_a.html"

driver.get(url)

ac = ActionChains(driver)

ac.pause(1)

driver.quit()