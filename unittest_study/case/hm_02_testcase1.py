# fighting AX
# 2025/5/6 10:54
'''
代码的目的：学习TestCase（测试用例）模块的书写方法

步骤
    1.导包
    2.自定义测试类，需要继承unittest模块中的TestCase类即可
    3.书写测试方法，即 用例代码
        书写要求：测试方法必须以 test_开头（本质是以test开头）
    4.执行用例（方法）
        光标放在 类名 运行，会执行类中的所有的测试方法
        光标放在 方法名 运行，只执行当前方法


'''

import unittest
class TestDemo1(unittest.TestCase):
    #用例代码
    def test_method1(self):
        print('测试方法1-1')

    def test_method2(self):
        print('测试方法1-2')
