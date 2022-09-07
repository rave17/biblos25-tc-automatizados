from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
import json

with open('../config/config.json', 'r') as file: config = json.load(file)

path = config['CHROME_ENV']['CHROME_PATH']
chrome_profile = config['CHROME_ENV']['CHROME_USER_PROFILE'].strip()
URL = config['BIBLOS']['URL']

chromeService = Service(path)

#setea las configuraciones del perfil a utilizar en chrome
options = Options()
options.add_argument(f'--user-data-dir={chrome_profile}')

driver = webdriver.Chrome(service=chromeService, options=options)

driver.get(URL)

wait_time_out = 10

wait = WDW(driver, wait_time_out)
driver.maximize_window

links = wait.until(EC.visibility_of_any_elements_located((By.TAG_NAME, "a")))
linksPrueba = wait.until(EC.visibility_of_element_located(By.PARTIAL_LINK_TEXT, "https://biblos"))

print("el link es: " + linksPrueba)


for link in links:
    print(link.text)
