from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Web_Sz.PageLocators.myapi_locators import MyApiLocators as mal
from Web_Sz.Common.basepage import BasePage


class IndexPage(BasePage):



    def isExist_logout_ele(self):
        #找到退出按钮就返回TRue
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,'//a[@class="account-logout"]')))
            return True
        except:
            return False

    #点击个人api
    def user_centor(self,men,women):
        #点击我的-个人中心
        # WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(mal.user_centor))
        doc = '点击api功能-测试生肖'
        self.wait_eleVisible(mal.user_centor,doc)
        # self.driver.find_element(*mal.user_centor).click()
        self.click_element(mal.user_centor,doc)
        #点击我的api进入
        # WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(mal.data_centor))
        self.wait_eleVisible(mal.data_centor, doc)
        # self.driver.find_element(*mal.data_centor).click()
        self.click_element(mal.data_centor, doc)
        # self.driver.find_element(*mal.user_centor_api).click()
        self.click_element(mal.user_centor_api, doc)
        #点击生肖配对接口
        # WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(mal.shengxiao_but))
        self.wait_eleVisible(mal.shengxiao_but, doc)
        # self.driver.find_element(*mal.shengxiao_but).click()
        self.click_element(mal.shengxiao_but, doc)
        #获取窗口句柄
        handles = self.driver.window_handles
        #切换到最新的窗口句柄
        self.driver.switch_to.window(handles[-1])
        # WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(mal.shengxiao_men_but))
        self.wait_eleVisible(mal.shengxiao_men_but, doc)
        # self.driver.find_element(*mal.shengxiao_men_but).send_keys(men)
        self.input_element(mal.shengxiao_men_but,text=men)
        # self.driver.find_element(*mal.shengxiao_women_but).send_keys(women)
        self.input_element(mal.shengxiao_women_but, text=women)
        # self.driver.find_element(*mal.ceshi_but).click()
        self.click_element(mal.ceshi_but,doc)
        # WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(mal.res_data))
        self.wait_eleVisible(mal.res_data, doc)
        # res = self.driver.find_element(*mal.res_data).text
        res = self.get_element(mal.res_data,doc)
        print(res)







