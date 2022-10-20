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

sleep(3)

a = driver.find_element(By.TAG_NAME, "a")
a.click()

p = driver.find_element(By.TAG_NAME, "p")

print(f"texto de a: {a.text}")
print(f"texto de p: {p.text}")

driver.quit()