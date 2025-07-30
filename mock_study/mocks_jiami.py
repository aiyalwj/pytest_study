# fighting AX
# 2025/5/22 13:55
import base64
import hashlib

from flask import Flask, request

# 1.初始化一个flask对象
app = Flask(__name__)

# 加密算法
# md5
def md5(value):
    # 对value做编码处理
    utf8_str = str(value).encode('utf-8')
    # 加密
    md5_str = hashlib.md5(utf8_str).hexdigest()
    # return md5_str.upper()
    return md5_str

# base64
def bs64(value):
    # 对value做编码处理
    utf8_str = str(value).encode('utf-8')
    # 加密
    # bs64_str = base64.b64encode(utf8_str) #返回的是b‘ 二进制的数据
    bs64_str = base64.b64encode(utf8_str).decode(encoding='utf-8') #将二进制值转换成字符串
    # return bs64_str.upper()
    return bs64_str


# 2.创建一个函数，并把这个函数装饰成一个mock server
@app.route('/mock', methods=['GET'])
def mockserver():
    print('mock server')
    return 'mock server'

@app.route('/study', methods=['GET','POST'])
def study():
    print('study')
    return {"name":"xiaoli","gender":"unknow"}

@app.route('/loginMD5', methods=['GET','POST'])
def md5_login():
    # 从请求里获得用户名和密码的值
    username = request.values.get("username")
    password = request.values.get("password")

    # 查询数据库中的用户名和密码 模拟
    db_user = "21232f297a57a5a743894a0e4a801fc3"
    db_pass = "202cb962ac59075b964b07152d234b70"
    if md5(username) == db_user and md5(password) == db_pass:
        return "登录成功"
    else:
        return "失败"

@app.route('/loginMD5postman', methods=['GET','POST'])
def md5_login_postman():
    # 从请求里获得用户名和密码的值
    username = request.values.get("username")
    password = request.values.get("password")

    # 查询数据库中的用户名和密码 模拟
    db_user = "admin"
    db_pass = "123"
    if username == md5(db_user) and password == md5(db_pass):
        return "登录成功"
    else:
        return "失败"

@app.route('/loginbase64', methods=['GET','POST'])
def bs64_login():
    # 从请求里获得用户名和密码的值
    username = request.values.get("username")
    password = request.values.get("password")

    # 查询数据库中的用户名和密码 模拟
    db_user = "YWRtaW4="
    db_pass = "MTIz"
    if bs64(username) == db_user and bs64(password) == db_pass:
        return "登录成功"
    else:
        return "失败"

@app.route('/loginbase64postman', methods=['GET','POST'])
def bs64_login_postman():
    # 从请求里获得用户名和密码的值
    username = request.values.get("username")
    password = request.values.get("password")

    # 查询数据库中的用户名和密码 模拟
    db_user = "admin"
    db_pass = "123"
    if username == bs64(db_user) and password == bs64(db_pass):
        return "登录成功"
    else:
        return "失败"

# 3.运行这个服务
if __name__ == '__main__':
    app.run()
    # print(md5("123"))
    # print(bs64("123"))