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

url = "https://selenium.dunossauro.live/caixinha"

driver.get(url)

ac = ActionChains(driver)

ac.pause(1)

caixa = driver.find_element(By.ID, 'caixa')
span = driver.find_element(By.TAG_NAME, 'span')

def caixinha(key1, key2=None):
    ac.pause(1)
    ac.key_down(key1)
    if key2:
        ac.key_down(key2)
    ac.move_to_element(caixa)
    ac.pause(1)
    ac.click()
    ac.pause(1)
    ac.double_click()
    ac.pause(1)
    ac.move_to_element(span)
    ac.pause(1)
    ac.key_up(key1)
    if key2:
        ac.key_up(key2)

ac.move_to_element(caixa)
ac.pause(1)
ac.click()
ac.pause(1)
ac.double_click()
ac.pause(1)
ac.move_to_element(span)
ac.pause(1)

caixinha(Keys.SHIFT)
caixinha(Keys.CONTROL)
caixinha(Keys.SHIFT, Keys.CONTROL)

ac.move_to_element(caixa)
ac.pause(1)
ac.context_click()
ac.pause(1)

ac.perform() 

ac.pause(1)

driver.quit()