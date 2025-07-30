# fighting AX
# 2025/5/8 20:30
'''
pytest  控制方法执行顺序插件
'''
import pytest

# @pytest.mark.run(order=2)
class TestDemo(object):
    # 语法：@pytest.mark.run(order=序号)
    @pytest.mark.run(order=3)
    def test_method1(self):
        print('测试方法1')

    @pytest.mark.run(order=2)
    def test_method2(self):
        print('测试方法2')

    @pytest.mark.run(order=1)
    def test_method3(self):
        print('测试方法3')

    '''
    拓展：序号支持正数和负数，以及正负混合
    1.纯正数：数越小，优先级越高（掌握）
    2.纯负数：数越小，优先级越高
    3.正负混合：正数先按照顺序执行，负数最后执行
    '''

#注意：控制方法执行顺序对测试类同样有效
# @pytest.mark.run(order=1)
# class TestDemo2(object):
#     def test_method1(self):
#         print('测试方法2-1')
