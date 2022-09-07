import json
from selenium import webdriver
from selenium.webdriver.common.by import By

with open('../config/config.json', 'r') as file: config = json.load(file)
chrome_profile = config['CHROME_ENV']['CHROME_USER_PROFILE'].strip()
urlNavegadorCarpeta = config['BIBLOS']['URL_NAV_CARP']

#Falta completar/definir DOM

class NavegadorCarpetas():
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.login = urlNavegadorCarpeta
        self.carpeta = "XPATH DE CARPETA"

    def editCarpeta(self):
        self.driver.find_element(By.XPATH, self.carpeta).click()

    @staticmethod
    def get_urlNavegadorCarpeta():
        return urlNavegadorCarpeta