import pytest
import json
from selenium import webdriver
from selenium.webdriver.common.by import By

with open('../config/config.json', 'r') as file: config = json.load(file)
urlLogin = config['BIBLOSD']['URL_LOGIN']


user = 'admin@dotcms.com'
password = 'admin'

class Login:
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.login = urlLogin
        self.userInput = "/html/body/dot-root/dot-login-page-component/div/dot-login-component/div/form/div[3]/span/input"
        self.passwordInput = "/html/body/dot-root/dot-login-page-component/div/dot-login-component/div/form/div[4]/span/input"
        self.userLoginBtn = "/html/body/dot-root/dot-login-page-component/div/dot-login-component/div/form/div[6]/button"

    def get_username(self):
        return self.driver.find_element(By.XPATH, self.userInput)

    def get_password(self):
        return self.driver.find_element(By.XPATH, self.passwordInput)

    def get_login_btn(self):
        return self.driver.find_element(By.XPATH, self.userLoginBtn)

    def doLogin(self, user, password):
        self.get_username().send_keys(user)
        self.get_password().send_keys(password)

        # boton login

    def doClickBtnLogin(self):
        self.get_login_btn().click()

    @staticmethod
    def get_urlLogin():
        return urlLogin
