import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By

with open('../config/config.json', 'r') as file: config = json.load(file)
chrome_profile = config['CHROME_ENV']['CHROME_USER_PROFILE'].strip()
urlBusquedaContenidos = config['BIBLOS']['URL_BUS_CONT']

class BusquedaContenidos():
    def __init__(self, driver):
        self.driver = driver
        self.url = urlBusquedaContenidos
        self.driver.switch_to.frame(0)
        self.dropDownCont = "/html/body/div[1]/form/div/div[1]/div/div[1]/dl/dd[1]/div/div[1]"
        self.opContentGeneric = "structure_inode_popup5"
        self.ordPorFechaAscDes = "Ultima fecha de edición"

    def getFilterContent(self):
        self.driver.find_element(By.XPATH, self.dropDownCont).click()
        self.driver.find_element(By.XPATH, self.opContentGeneric).click()

    def doOrdernarAscDesc(self):
        self.driver.find_element(By.LINK_TEXT, self.ordPorFechaAscDes).click()

