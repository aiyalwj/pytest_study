# fighting AX
# 2025/5/11 19:20
import json

import requests


response = requests.get('http://mirrors.sohu.com/')

'''
requests是 以什么编码格式 把HTTP响应消息体中的 字节串 解码 为 字符串的呢？
requests 会根据响应消息头（比如 Content-Type）对编码格式做推测。
但是有时候，服务端并不一定会在消息头中指定编码格式，这时， requests的推测可能有误，需要我们指定编码格式。
'''
print('1-------------------')
print('---encode')
print(response.encoding)
response.encoding='utf8'
print('---text')
# 获取响应的消息体的文本内容，直接通过response对象 的 text 属性即可获取
print(response.text)

# 直接获取字节串的内容
print('2-------------------')
print('---content')
print(response.content)
print('---contentutf8')
print(response.content.decode('utf8'))# 解码

print('3-------------------')
response = requests.post("http://httpbin.org/post", data={1:1,2:2})
# loads解码 将 JSON 格式的字符串反序列化为 Python 数据结构（如字典、列表等）
obj = json.loads(response.content.decode('utf8'))

#简化
# obj = response.json()
print(obj)