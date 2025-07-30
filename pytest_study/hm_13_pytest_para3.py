# fighting AX
# 2025/5/8 21:06
'''
pytest参数化功能：通过方法引入数据
'''
import pytest

def build_test_data():
    return [('admin',123456),('test',654321),('xxx','yyy')]

class TestDemo(object):
    # 语法 @pytest.mark.parametrize('参数变量1,参数变量2',[(数据1-1,数据1-2),(数据2-1,数据2-2),...])
    # 注意:
    # 1.多个参数必须置于同一个字符串内!
    # 2.数据格式必须是:[(),()]或者[[]，[]]
    @pytest.mark.parametrize(('name,pwd'),build_test_data())
    def test_method1(self,name,pwd):
        print('账号:{} 密码:{}'.format(name, pwd))

if __name__ == '__main__':
    pytest.main(['-s', 'hm_13_pytest_para3.py'])