# fighting AX
# 2025/5/6 17:28
'''
对于一些未完成的或者不满足测试条件的测试函数和测试类，可以跳过执行
代码书写在TestCase文件

#直接将测试函数标记为跳过
@unittest.skip('代码未完成'）
#根据条件判断测试函数是否跳过，判断条件成立没跳过
@unittest.skipIf(condition,reason）

'''
import unittest

version = 30

class TestDemo(unittest.TestCase):
    @unittest.skip('不想执行')
    def test_1(self):
        print('测试方法1')

    @unittest.skipIf(version >= 30,'版本大于等于30，不用测试')
    def test_2(self):
        print('测试方法2')

    def test_3(self):
        print('测试方法3')