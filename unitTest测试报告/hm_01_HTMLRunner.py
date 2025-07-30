# fighting AX
# 2025/5/6 17:52

import unittest
from HTMLTestRunnerCN import HTMLTestRunner

suit = unittest.defaultTestLoader.discover('../unittest_study','hm_11_assert.py')
'''
stream=sys.stdout,  必填，测试报告的文件对象（open），要使用wb打开
verbosity=1, 可选，报告的详细程度，默认1简略，2详细
title=None, 可选，测试报告的标题
description=None, 可选，描述信息，python的版本，pycharm版本
'''

file = 'report.html'
with open(file,'wb') as f:
    runner = HTMLTestRunner(f,2,'unitTest测试报告','python3.8')

    runner.run(suit)