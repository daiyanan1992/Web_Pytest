import unittest
from selenium import webdriver
from Web_Sz.TestDatas import Common_Datas as CD
from Web_Sz.PageObjects.login_page import LoginPage
from Web_Sz.PageObjects.index_page import IndexPage
from Web_Sz.TestDatas import login_datas as LD
from ddt import ddt,data,unpack


@ddt
class TestApi(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()  # 访问谷歌驱动
        cls.driver.get(CD.web_login_url)  # 打开url
        cls.driver.maximize_window()
        LoginPage(cls.driver).login('18018039181', 'huahua1002')  # 实现已登录功能

    # def setUp(self):
    #     self.driver = webdriver.Chrome()#访问谷歌驱动
    #     self.driver.get(CD.web_login_url)#打开url
    #     self.driver.maximize_window()
    #     LoginPage(self.driver).login('18018039181','huahua1002')#实现已登录功能

        # 正常测试用例
        # 前提条件
        # 1、用户已登录

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # def tearDown(self):
    #     self.driver.quit()

    @data(*LD.shengxiao_data)
    def test_my_api_success_shengxiao(self,data):
        IndexPage(self.driver).user_centor(data['men'],data['women'])
        # 步骤：
        # 1、点击：我的api 2、点击生肖配对的测试按钮//a[text()="生肖配对"]/ancestor::div/div/p/a
        # 切换窗口
        # ，3切换窗口输入生肖4、点击测试



