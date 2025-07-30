# fighting AX
# 2025/5/6 11:55
'''
代码的目的：学习TestLoader 的使用

步骤
    1.导包
    2.实例化测试加载对象并添加用例 得到的是suite对象
        方法一：unittest.TestLoader().discover('用例所在的路径','用例的代码文件名')
                用例所在的路径 建议使用相对路径
                用例的代码文件名 可以使用 * 通配符
        方法二：使用默认的加载对象并加载用例
    3.实例化运行对象
    4.使用运行对象去执行套件对象
        运行对象.run（套件对象）

    34步可以简化unittest.TextTestRunner.run(suite)

在一个项目中TestCase的代码，一般放在一个单独的目录case
'''
import unittest

# 方法一
suite = unittest.TestLoader().discover('./case','hm*.py')
# suite = unittest.TestLoader().discover('./case','*_test*.py')

# 方法二
suite = unittest.defaultTestLoader.discover('./case','hm*.py')

runner = unittest.TextTestRunner()

runner.run(suite)

# unittest.TextTestRunner.run(suite)
