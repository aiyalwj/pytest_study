# fighting AX
# 2025/5/6 19:49
'''
特殊方法：函数级别
'''
import pytest


class TestDemo(object):
    # 说明：特殊方法名写法固定，没有代码提示，需要手写！
    # 注意函数级别执行顺序：先setup（） -> 测试方法 -> teardown（）

    # 开始方法
    def setup_method(self):
        print('函数——>开始')

    # 结束方法
    def teardown_method(self):
        print('函数——>结束')

    def test_method1(self):
        print('测试方法1')

    def test_method2(self):
        print('测试方法2')

if __name__ == '__main__':
    # pytest.main(['-s', '文件名.py'])
    pytest.main(['-s','hm_05_pytest_basic_05.py'])