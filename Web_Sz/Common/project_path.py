import os




path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
# print(path)


# D:\Web_python2\Python_jehu\test_result\html_report\test_juhe_report_new.html
#测试报告地址D:\Web_pythonNew\Web_Sz\Outputs\report
HtmlReport_path=path+'\\Outputs\\report\\test_juhe_report_new.html'

#日志打印地址D:\Web_pythonNew\Web_Sz\Outputs\logs
Log_path=path+'\\Outputs\\logs\\Web_pythonNew.txt'
# print(Log_path)
#文件目录地址D:\Web_python2\Python_jehu\test_data\test_case925.xlsx
Dir_path=path+'\\test_data\\test_case925.xlsx'
# print(Dir_path)

#截图保存路劲D:\Web_pythonNew\Web_Sz\Outputs\screenshots
Screen_path = path+'\\Outputs\\screenshots'
# print(Screen_path)
# file_name = Screen_path+'\\{0}_{1}'.format('dai','2020-10-22 16:24:47.435326')
# print(file_name)

#testcase_dir测试用例文件路劲D:\Web_pythonNew\Web_Sz\TestCases
testcase_dir = path+'\\TestCases'