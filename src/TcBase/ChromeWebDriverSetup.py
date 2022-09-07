import json
from selenium import webdriver
import urllib3

with open('../../config/config.json', 'r') as file: config = json.load(file)
chrome_profile = config['CHROME_ENV']['CHROME_USER_PROFILE'].strip()

class WebDriver():
    def setUp(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        if self.driver is not True:
            self.driver.close()
            self.driver.quit()

