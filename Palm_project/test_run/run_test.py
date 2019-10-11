# -*- coding: utf-8 -*-
import unittest
from BeautifulReport import BeautifulReport
from Palm_project.test_run.sendmail import send_mail

# 用例存放位置
test_case_path="/Users/lcy/Documents/GitHub/Palm_test_project/Palm_project/test_case"
# 测试报告存放位置
log_path='/Users/lcy/Documents/GitHub/Palm_test_project/Palm_project/reports'
# 测试报告名称
filename='Palm Secret test report'
#用例名称
description='Palm Secret Test'
# 需要执行哪些用例，如果目录下的全部，可以改为"*.py"，如果是部分带test后缀的，可以改为"*test.py"
pattern="test010_psychological.py"

if __name__ == '__main__':
    test_suite = unittest .defaultTestLoader.discover(test_case_path, pattern=pattern)
    result = BeautifulReport(test_suite)
    result.report(filename=filename,description=description,log_path=log_path)

