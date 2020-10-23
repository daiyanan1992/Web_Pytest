import unittest
from Web_Sz.Common import project_path as PP
import HTMLTestRunner




#suite存储用例
suite = unittest.TestSuite()

#方法二 TEstLoader
loader = unittest.TestLoader()#创建一个加载器

#使用discover去找一个目录下所有测试用例
suite.addTests(loader.discover(PP.testcase_dir))

with open(PP.HtmlReport_path,'wb') as file:
    runner =  HTMLTestRunner.HTMLTestRunner(stream=file, verbosity=2, title='聚合数据测试报告',
                                            description='聚合测试自动化测试报告')
    runner.run(suite)