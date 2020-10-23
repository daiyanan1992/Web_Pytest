from Web_Sz.Common.my_log import My_Log
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from Web_Sz.Common import project_path as PP

#封装基本函数 执行日志 异常处理 失败截图
class BasePage:
    def __init__(self,driver):
        self.driver = driver

    #等待元素课件
    def wait_eleVisible(self,locator,doc=''):
        '''
        :param locator:定位表达式
        :param times:超时时间
        :param poll_frequency:
        :param doc:读取调用的模块名
        :return:
        '''
        My_Log().my_log('等待元素{0}可见'.format(locator),'INFO')
        try:
            #开始等待的时间
            start = datetime.now()
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locator))
            #结束等待时间
            end = datetime.now()
            #球一个差值写在日志中
            durn = (end-start).seconds
            My_Log().my_log('等待时长为{}'.format(str(durn)), 'INFO')
            # logging.info('等待时长为{}'.format())
            self.save_screenshot(doc)
        except:
            My_Log().my_log('等待元素课件失败！！！', 'ERROR')
            # logging.exception('等待元素课件失败！！！')
            self.save_screenshot(doc)
            raise #异常抛出

    #等待元素存在

    #查找元素-记得返回元素
    def find_element(self,locator,doc=''):
        My_Log().my_log('等待元素{0}可见'.format(locator), 'INFO')
        try:
            return self.driver.find_element(*locator)
        except:
            My_Log().my_log('查找元素失败！！！', 'ERROR')
            self.save_screenshot(doc)
            raise



    #点击操作
    def click_element(self,locator,doc=''):
        My_Log().my_log('点击元素{0}开始'.format(locator), 'INFO')
        #找元素
        ele = self.find_element(locator)
        #元素操作
        try:
            ele.click()
            self.save_screenshot(doc)
        except:
            My_Log().my_log('点击元素失败！！！', 'ERROR')
            self.save_screenshot(doc)
            raise

    #输入操作
    def input_element(self,locator,text,doc=''):
        My_Log().my_log('插入元素{0}开始'.format(locator), 'INFO')
        ele = self.find_element(locator)
        try:
            ele.send_keys(text)
            self.save_screenshot(doc)
        except:
            My_Log().my_log('输入元素！！！', 'ERROR')
            self.save_screenshot(doc)
            raise

    #获取文本内容
    def get_element(self,locator,doc):
        My_Log().my_log('获取元素{0}开始'.format(locator), 'INFO')
        ele = self.find_element(locator)
        try:
            ele.text
        except:
            My_Log().my_log('元素文本查找失败！！！', 'ERROR')
            self.save_screenshot(name=doc)
            raise

    #获取元素属性


    #窗口切换


    #截图
    def save_screenshot(self,name):
        #图片名称：模块名-页面名称-操作名称-时间.png
        file_name = PP.Screen_path+'\\{0}_ceshi.png'.format(name)
        # print(file_name)
        self.driver.save_screenshot(file_name)
        # logging.info('截取成功，文件路径为：{}'.format(file_name))
        My_Log().my_log('截取成功，文件路径为：{}'.format(file_name), 'INFO')

