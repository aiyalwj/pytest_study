# fighting AX
# 2025/5/6 14:47
import unittest

class TestLogin(unittest.TestCase):
    def setUp(self):
        print('输入网址......')

    def tearDown(self):
        print('关闭当前页面......')

    @classmethod
    def setUpClass(cls):
        print('------1.打开浏览器')

    @classmethod
    def tearDownClass(cls) -> None:
        print('------5.关闭浏览器')


    def test_1(self):
        print('输入正确用户名密码验证码，点击登录 1')

    def test_2(self):
        print('输入错误用户名密码验证码，点击登录 2')