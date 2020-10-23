from selenium.webdriver.common.by import By



class LoginPageLocators:
    name_text = (By.XPATH,'//input[@id="username"]')
    pwd_text = (By.XPATH,'//input[@id="password"]')
    login_button = (By.XPATH,'//input[@id="loginBtn"]')

    #空用户名报错定位
    null_username = (By.XPATH,'//em[text()="请输入正确格式的用户名!"]')

    #错误的用户名
    error_username = (By.XPATH,'//div[@class="sysError"]')