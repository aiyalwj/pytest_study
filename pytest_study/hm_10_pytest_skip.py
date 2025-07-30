# fighting AX
# 2025/5/8 20:58
'''
跳过功能
'''
import pytest

version = 25

class TestDemo(object):
    def test_method1(self):
        print('测试方法1')
    '''
    语法: @pytest.mark.skipif(符合的条件, reason='跳过的原因')
    说明: 如果满足条件, 以下方法或测试类执行跳过, 不执行!
    注意: reason= 不能省略, 否则报错!
    @pytest.mark.skipif(version >= 25, 'xxx') # 错误样例
    '''
    @pytest.mark.skipif(version >= 25, reason='xxx')
    def test_method2(self):
        print('测试方法2')

    def test_method3(self):
        print('测试方法3')


# 说明:同样可以跳过测试类
@pytest.mark.skipif(version>= 25,reason='当前版本不执行')
class TestDemo2(object):
    def test_method(self):
        print('测试类2 -> 测试方法')

if __name__ == '__main__':
    pytest.main(['-s', 'hm10_pytest_skip.py'])