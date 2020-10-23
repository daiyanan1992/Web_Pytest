import pytest
from selenium import webdriver
from Web_Sz.TestDatas import Common_Datas as CD
from Web_Sz.PageObjects.login_page import LoginPage
import sys,os

sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__)))))
# 告诉pytest运行前先检索当前路径

# sys.path.append(os.getcwd())

driver = None

@pytest.fixture(scope='class')
def access_web():
    #前置条件
    global driver
    driver = webdriver.Chrome()
    driver.get(CD.web_login_url)
    driver.maximize_window()
    lg = LoginPage(driver)
    yield(driver,lg) #分割线 后面存在返回的功能
    driver.quit()
    #后置条件



