from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Web_Sz.PageLocators.loginpage_locators import LoginPageLocators as loc

class LoginPage:

    #页面只需要传参即可，用例打开流量器就行
    def __init__(self,driver):
        self.driver = driver

    #登录
    def login(self,username,passwd):
        # name_text = '//input[@id="username"]'
        # pwd_text = '//input[@id="password"]'
        # login_button = '//input[@id="loginBtn"]'
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(loc.name_text))
        self.driver.find_element(*loc.name_text).send_keys(username)
        self.driver.find_element(*loc.pwd_text).send_keys(passwd)
        self.driver.find_element(*loc.login_button).click()

    #登录空用户名
    def isUserNameLoginEle(self):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc.null_username))
            return True
        except:
            return False
    #错误用户名及密码
    def errorUserNameLoginEle(self):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc.error_username))
        return self.driver.find_element(*loc.error_username).text

    #注册
    def register(self):
        pass

    #忘记密码