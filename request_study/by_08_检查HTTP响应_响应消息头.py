# fighting AX
# 2025/5/11 19:20
import json

import requests


response = requests.get('http://www.baidu.com/')
print(type(response.headers))# 继承自dict的子类
print(dict(response.headers))