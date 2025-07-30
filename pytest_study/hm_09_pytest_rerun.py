# fighting AX
# 2025/5/8 20:30
'''
pytest  失败重试插件
'''

class TestDemo(object):
    def test_method1(self):
        print(1/0)