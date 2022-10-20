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

url = "https://curso-python-selenium.netlify.app/aula_03.html"

driver.get(url)

sleep(1)

a = driver.find_element(By.TAG_NAME, "a")
p = driver.find_element(By.TAG_NAME, "p")

for click in range(11):
    a.click()
    ps = driver.find_elements(By.TAG_NAME, "p")
    print(f"valor do ultimo p {ps[-1].text}")
    print(f"valor do click: {click}")

# print(f"texto de a: {a.text}")
# print(f"texto de p: {p.text}")

# driver.quit()