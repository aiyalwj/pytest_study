# fighting AX
# 2025/5/6 20:19

#测试类形式
class TestDemo(object): #要求测试类名以test开头
    def test_method1(self): #要求测试方法名以test开头
        print('测试方法2-1')

    def test_method2(self):
        print('测试方法2-2')

if __name__ == '__main__':
    # pytest.main(['-s', '文件名.py'])
    pytest.main(['-s','hm_04_pytest_basic_04.py'])