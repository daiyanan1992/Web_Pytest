from selenium import webdriver
from Web_Sz.PageObjects.login_page import LoginPage
from Web_Sz.PageObjects.index_page import IndexPage
from Web_Sz.TestDatas import Common_Datas as CD
from Web_Sz.TestDatas import login_datas as LD
import pytest


@pytest.mark.usefixtures('access_web')
class TestLogin:

    # def setUp(self):
    #     #前置访问页面
    #     self.driver = webdriver.Chrome()
    #     self.driver.get(CD.web_login_url)
    #     self.driver.maximize_window()
    #     self.lg = LoginPage(self.driver)
    #
    # def tearDown(self):
    #     self.driver.quit()

    #正常登录 fixture的函数名称 用来接收他的返回值
    @pytest.mark.smoke
    def test_login_success(self,access_web):
        #前置 访问登录页面
        #步骤 输入用户名密码点击登录
        access_web[1].login(LD.success_data['user'],LD.success_data['passwd'])
        #断言 首页当中是否找到什么元素
        assert IndexPage(access_web[0]).isExist_logout_ele()#新表达式

  # 错误登录
    @pytest.mark.parametrize('data',LD.phone_data)
    def test_login_success(self,data,access_web):
        #前置 访问登录页面
        #步骤 输入用户名密码点击登录
        access_web[1].login(data['user'],data['passwd'])
        #断言 首页当中是否找到什么元素
        # self.assertTrue(self.lg.errorUserNameLoginEle())
        assert access_web[1].errorUserNameLoginEle()== data['check']
