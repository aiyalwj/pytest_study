# fighting AX
# 2025/5/8 21:41
'''
pytest 断言
'''
import pytest
def add_func(num1, num2):
    return num1 + num2


class TestDemo(object):
    def test_method(self):
        result = add_func(1,2)
        assert 3 == result
        # assert 4 == result

if __name__ == '__main__':
    pytest.main(['-s', 'hm_15_pytest_assert.py'])