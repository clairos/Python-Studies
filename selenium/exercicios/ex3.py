from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from pprint import pprint # pretty print

# cria a instância do driver do navegador
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wdw = WebDriverWait(driver, 10)

url = "https://curso-python-selenium.netlify.app/exercicio_03.html"

driver.get(url)

sleep(1)

def find_links(driver, elemento):
    element = driver.find_element(By.TAG_NAME, elemento)
    a = element.find_elements(By.TAG_NAME, 'a')
    return a

a1 = driver.find_elements(By.TAG_NAME, 'a')
print(a1[-1].text)
a1[-1].click()

sleep(1)

a2 = find_links(driver, 'main')

for a in a2:
    if a.get_attribute('attr') == 'errado':
        a.click()

sleep(1)

driver.quit()