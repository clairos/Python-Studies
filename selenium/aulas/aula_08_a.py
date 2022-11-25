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

texto = 'clara'

# high level
elemento = driver.find_element(By.NAME, 'texto')
elemento.send_keys(texto)
sleep(1)

# low level
ac = ActionChains(driver)
ac.move_to_element(elemento)
ac.click(elemento)

def digita(key):
    # ac.key_down(u'\ue008') # utilizando unicode code point
    ac.key_down(key) # utilizando a biblioteca Keys

    for letra in texto:
        ac.key_down(letra)
        ac.key_up(letra)

    # ac.key_down(u'\ue008')
    ac.key_up(key)

digita(Keys.SHIFT)
# digita(Keys.CAPS_LOCK)

ac.perform()

# https://www.selenium.dev/pt-br/documentation/webdriver/actions_api/keyboard/
# https://www.w3.org/TR/webdriver/#keyboard-actions

sleep(1)

driver.quit()