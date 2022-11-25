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
from time import sleep

# cria a instância do driver do navegador
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wdw = WebDriverWait(driver, 10)

url = "https://selenium.dunossauro.live/aula_08_a"

driver.get(url)

sleep(1)

texto = 'Clara'

# high level
elemento = driver.find_element(By.NAME, 'texto')
elemento.send_keys(texto)

sleep(1)

# low level
ac = ActionChains(driver)
# ac.key_down(u'\ue008') # utilizando unicode code point
ac.key_down(Keys.SHIFT) # utilizando a biblioteca Keys
ac.key_down(texto[2])
ac.key_up(texto[2])
# ac.key_down(u'\ue008')
ac.key_up(Keys.SHIFT)
ac.perform()

# https://www.selenium.dev/pt-br/documentation/webdriver/actions_api/keyboard/
# https://www.w3.org/TR/webdriver/#keyboard-actions

sleep(3)

driver.quit()
