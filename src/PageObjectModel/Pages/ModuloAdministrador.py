import json
from selenium import webdriver
from selenium.webdriver.common.by import By

with open('../config/config.json', 'r') as file: config = json.load(file)
chrome_profile = config['CHROME_ENV']['CHROME_USER_PROFILE'].strip()
urlModuloAdm = config['BIBLOS']['URL_MOD_ADM']
wait_time_out = 10



class ModuloAdministrador():
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.moduloAdm = urlModuloAdm
        #listado de hosts
        self.dropDownListaHosts = "/html/body/dot-root/dot-main-component/div/header/dot-toolbar/p-toolbar/div/div[2]/dot-site-selector/dot-searchable-dropdown/button/span[1]"
        self.hostBiblos = "/html/body/div/div/p-dataview/div/div[2]/div/span[1]"
        self.hostCds = "/html/body/div/div/p-dataview/div/div[2]/div/span[2]"
        self.hostCsp = "/html/body/div/div/p-dataview/div/div[2]/div/span[3]"
        self.hostFichas = "/html/body/div/div/p-dataview/div/div[2]/div/span[4]"
        self.hostIpp = "/html/body/div/div/p-dataview/div/div[2]/div/span[5]"
        self.hostNews = "/html/body/div/div/p-dataview/div/div[2]/div/span[6]"
        self.hostNovedades = "/html/body/div/div/p-dataview/div/div[2]/div/span[7]"
        self.hostPan = "/html/body/div/div/p-dataview/div/div[2]/div/span[8]"
        self.hostSoporte = "/html/body/div/div/p-dataview/div/div[2]/div/span[9]"
        self.hostUrgencias = "/html/body/div/div/p-dataview/div/div[2]/div/span[10]"

    def filterHost(self):
        self.driver.find_element(By.XPATH, self.listaHosts).click()
#falta definir seleccion de host
    @staticmethod
    def get_urlModuloAdm():
        return urlModuloAdm