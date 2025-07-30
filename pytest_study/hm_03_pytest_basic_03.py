# fighting AX
# 2025/5/6 19:18

# 先 pip install pytest 安装pytest包

#函数形式
import pytest


def test_func(): #要求函数名以test开头
    # 测试函数
    print('我是测试函数')

if __name__ == '__main__':
    # pytest.main(['-s', '文件名.py'])
    pytest.main(['-s','hm_03_pytest_basic_03.py'])