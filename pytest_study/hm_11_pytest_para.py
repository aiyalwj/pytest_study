# fighting AX
# 2025/5/8 21:06
'''
pytest参数化功能：单个参数
'''
import pytest


class TestDemo(object):
    # 语法 @pytest.mark.parametrize('参数变量',['数值1','数值2',...])
    # 多少个数值就测试多少次
    @pytest.mark.parametrize('name', ['小明', '小刚'])
    def test_method1(self,name):
        print('获取的名字是：',name)

if __name__ == '__main__':
    pytest.main(['-s', 'hm_11_pytest_para.py'])