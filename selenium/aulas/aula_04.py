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

url = "https://curso-python-selenium.netlify.app/aula_04.html"

driver.get(url)

sleep(1)

aside = driver.find_element(By.TAG_NAME, 'aside')

aside_as = aside.find_elements(By.TAG_NAME, 'a')

links_aulas = {}

for a in aside_as:
    links_aulas[a.text] = [a.get_attribute('href')]

pprint(links_aulas)
aula_3 = str(links_aulas['Aula 3']).split("'")
new_url = aula_3[1]
print(new_url)

driver.get(new_url)

driver.back()

# main = driver.find_element(By.TAG_NAME, 'main')



driver.quit()