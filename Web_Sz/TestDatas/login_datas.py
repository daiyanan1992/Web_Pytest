



#正常场景 -测试数据
success_data = {'user':"18018039181",'passwd':'huahua1002'}

#异常用例 -手机号码不正确
phone_data = [
    {'user':'180180391811','passwd':'huahua1002','check':'登录失败,请确认账号和密码正确'},
    {'user':'1801803918','passwd':'huahua1002','check':'请输入正确格式的用户名!'},
    {'user':'', 'passwd': 'huahua1002', 'check': '请输入正确格式的用户名!'},
    {'user':'18018039181', 'passwd': 'huahua10021', 'check': '登录失败,请确认账号和密码正确'},
]

#生肖组合数据
shengxiao_data=[
    {'men':'猴','women':'鼠'},
    {'men':'猴','women':'猪'}
]