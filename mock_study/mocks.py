# fighting AX
# 2025/5/22 13:55
from flask import Flask

# 1.初始化一个flask对象
app = Flask(__name__)


# 2.创建一个函数，并把这个函数装饰成一个mock server
@app.route('/mock', methods=['GET'])
def mockserver():
    print('mock server')
    return 'mock server'

@app.route('/study', methods=['GET','POST'])
def study():
    print('study')
    return {"name":"xiaoli","gender":"unknow"}

# 3.运行这个服务
if __name__ == '__main__':
    app.run()
