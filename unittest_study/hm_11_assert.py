# fighting AX
# 2025/5/6 14:47
'''
代码的目的：学习断言assert 的使用

断言的结果有两种：
    True，用例通过
    False，代码抛出异常，用例不通过

assertEqual（预期结果，实际结果） #判断预期结果和实际结果是否相等
1.如果相等，用例通过
2.如果不相等，用例不通过，抛出异常

assertIn（预期结果，实际结果） #判断预期结果是否包含在实际结果中
1.包含，用例通过
2.不包含，用例不通过，抛出异常

'''

import unittest

def add(a,b):
    return a+b


class TestAdd(unittest.TestCase):
    def test_method1(self):
        self.assertEqual(3,add(1,2))

    def test_method2(self):
        self.assertEqual(30,add(10,20))

    def test_method3(self):
        # self.assertEqual(5,add(2,3))
        self.assertEqual(6,add(2,3))