#!/Users/lcy/ok/GitHub/bin/python3.7
# -*- coding: utf-8 -*-

import os
os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import unittest
from BeautifulReport import BeautifulReport
from test_run.sendmail import send_mail

# sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/Users/lcy/Documents/GitHub/Palm_test_project/Palm_project")

# 用例存放位置
test_case_path="/Users/lcy/Documents/GitHub/Palm_test_project/Palm_project/test_case"
# 测试报告存放位置
log_path='/Users/lcy/Documents/GitHub/Palm_test_project/Palm_project/reports'
# 测试报告名称
filename='Palm Secret test report'
#用例名称
description='Palm Secret Test'
# 需要执行哪些用例，如果目录下的全部，可以改为"*.py"，如果是部分带test后缀的，可以改为"*test.py"
# pattern = "test001_homepage_enter.py"
# pattern = "test002_information_write.py"
# pattern = "test003_palm_judge.py"
# pattern = "test004_constellation_match.py"
# pattern = "test005_constellation_enter.py"
# pattern = "test006_constellation_everyday.py"
# pattern = "test007_tarot_everyday.py"
# pattern = "test008_old_face_enter.py"
# pattern = "test009_old_face_get_by_photo.py"
# pattern = "test010_psychological.py"
# pattern = "test011_today_page.py"
pattern = "test*.py"

if __name__ == '__main__':
    test_suite = unittest .defaultTestLoader.discover(test_case_path, pattern=pattern)
    result = BeautifulReport(test_suite)
    result.report(filename=filename,description=description,log_path=log_path)
    file_new = '/Users/lcy/Documents/GitHub/Palm_test_project/Palm_project/Palm Secret test report.html'
    send_mail(file_new)

