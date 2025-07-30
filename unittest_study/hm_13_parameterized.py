# fighting AX
# 2025/5/6 16:39
'''
代码的目的：学习parameterized 的使用

1.导包unittest
2.定义测试类
3.书写测试方法（用到的测试数据使用变量代替）
4.组织测试数据并传参
    [(),(),()] or [[],[],[]]

'''
import json
import unittest
from parameterized import parameterized
from unittest_study.hm_05_demo1 import add

# data = [
#     (3,1,2),
#     (30,10,20),
#     (5,2,3)
# ]

def build_data():
    with open('data.json','r',encoding='utf-8') as f:
        result = json.load(f)
        data = []
        for i in result:
            data.append((i.get('expect'),i.get('x'),i.get('y')))
    return data


class TestLogin(unittest.TestCase):
    # @parameterized.expand(data)
    @parameterized.expand(build_data())
    #数据和参数要保持一致
    def test_login(self, expect, x, y):
        self.assertEqual(expect,add(x,y))