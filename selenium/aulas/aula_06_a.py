from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # type: ignore
from selenium.webdriver.common.by import By  # type: ignore
from selenium.webdriver.common.keys import Keys  # type: ignore
from webdriver_manager.chrome import ChromeDriverManager  # type: ignore
from selenium.webdriver.support.ui import WebDriverWait  # type: ignore
from selenium.webdriver.support import expected_conditions as EC  # type: ignore
from time import sleep

# cria a instância do driver do navegador
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wdw = WebDriverWait(driver, 10)

url = 'https://curso-python-selenium.netlify.app/aula_06_a.html'

driver.get(url)

sleep(1)

# nome = driver.find_element(By.CSS_SELECTOR, '[type="text"]')
# senha = driver.find_element(By.CSS_SELECTOR, '[type="password"]')
# btn = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')

# nome = driver.find_element(By.CSS_SELECTOR, '[name="text"]')
# senha = driver.find_element(By.CSS_SELECTOR, '[name="password"]')
# btn = driver.find_element(By.CSS_SELECTOR, '[name="submit"]')

# nome = driver.find_element(By.CSS_SELECTOR, '[name*="ome"]')
# senha = driver.find_element(By.CSS_SELECTOR, '[name*="nha"]')
# btn = driver.find_element(By.CSS_SELECTOR, '[name*="l0"]')

# nome = driver.find_element(By.CSS_SELECTOR, '[name|="nome"]')
# senha = driver.find_element(By.CSS_SELECTOR, '[name|="senha"]')
# btn = driver.find_element(By.CSS_SELECTOR, '[name|="l0c0"]')

nome = driver.find_element(By.CSS_SELECTOR, '[name^="n"]')
senha = driver.find_element(By.CSS_SELECTOR, '[name^="s"]')
btn = driver.find_element(By.CSS_SELECTOR, '[name^="l"]')

nome.send_keys('Clara')
senha.send_keys('submarino123')
btn.click()

sleep(2)

driver.quit()