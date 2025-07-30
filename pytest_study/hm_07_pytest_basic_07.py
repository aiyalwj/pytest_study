# fighting AX
# 2025/5/6 19:49
'''
特殊方法：函数级别和类级别同时使用
'''
import pytest


class TestDemo(object):
    # 执行顺序13543642


    def setup_class(self): #1
        print('类级别——>开始')
    def teardown_class(self): #2
        print('类级别——>结束')


    def setup_method(self): #3
        print('函数级别——>开始')
    def teardown_method(self): #4
        print('函数级别——>结束')


    def test_method1(self): #5
        print('测试方法1')

    def test_method2(self): #6
        print('测试方法2')

if __name__ == '__main__':
    # pytest.main(['-s', '文件名.py'])
    pytest.main(['-s','hm_07_pytest_basic_07.py'])