from selenium.webdriver.common.by import By


class MyApiLocators:
    #登录后-右上角个人中心
    user_centor = (By.XPATH,'//a[contains(text(),"个人中心")]')
    #数据中心按钮
    data_centor = (By.XPATH,'//span[text()="数据中心"]')
    #数据中心-我的api
    user_centor_api = (By.XPATH,'//div[text()="我的API"]')
    #生肖配对测试按钮
    shengxiao_but = (By.XPATH,'//a[text()="生肖配对"]/ancestor::div/div/p/a')
    #接口输入男生肖按钮
    shengxiao_men_but = (By.XPATH,'//input[@data="men"]')
    # 接口输入女生肖按钮
    shengxiao_women_but = (By.XPATH, '//input[@data="women"]')
    # 接口发送按钮
    ceshi_but = (By.XPATH, '//button[@id="boxBtn"]')
    #返回数据data定位
    res_data = (By.XPATH, '//span[text()="data"]/following::span/span[@class="hljs-string"]')