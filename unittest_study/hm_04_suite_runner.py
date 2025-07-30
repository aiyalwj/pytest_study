# fighting AX
# 2025/5/6 11:55
'''
代码的目的：学习TestSuite 和 TestRunner 的使用

步骤
    1.导包
    2.实例化（创建对象）套件对象
    3.使用套件对象添加用例方法
        方式一：套件对象.addTest（测试类名（‘方法名’））
        方式一：将一个测试类中的所有方法进行添加 套件对象.addTest（unitest.makeSuite（测试类名））
    4.实例化运行对象
    5.使用运行对象去执行套件对象
        运行对象.run（套件对象）
'''
import unittest
from unittest_study.case.hm_02_testcase1 import TestDemo1
from unittest_study.case.hm_03_testcase2 import TestDemo2

suit = unittest.TestSuite()

# 写法一
# suit.addTest(TestDemo1('test_method1'))
# suit.addTest(TestDemo1('test_method2'))
# suit.addTest(TestDemo2('test_method1'))
# suit.addTest(TestDemo2('test_method2'))

# 写法二
suit.addTest(unittest.makeSuite(TestDemo1))
suit.addTest(unittest.makeSuite(TestDemo2))

runner = unittest.TextTestRunner()

runner.run(suit)

'''
终端运行
....

.表示用例通过
F表示用例不通过
E表示用例代码有问题
'''