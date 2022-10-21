from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# cria a instância do driver do navegador
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wdw = WebDriverWait(driver, 10)

url = "https://curso-python-selenium.netlify.app/exercicio_01.html"

driver.get(url)

sleep(1)

title = driver.find_element(By.TAG_NAME, 'h1')

d1 = {title.text: 'Vazio'}
print(d1)
d2 = {}

for i in range(3):
    p = driver.find_elements(By.TAG_NAME, 'p')
    d2.update({f'texto{i+1}': p[i].text})

d1 = {title.text: d2}

print(d1)

driver.quit()
