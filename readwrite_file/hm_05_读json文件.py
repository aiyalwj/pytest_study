# fighting AX
# 2025/5/5 19:39
'''
读取json文件
    1.导包import json
    2.读打开文件
    3.读文件
    json.load(文件对象)
返回的是 字典（文件中是对象）或者列表（文件中是数组）
'''
import json
with open('info.json', 'r', encoding='utf-8') as f:
    # buf = f.read()
    # print(type(buf),buf)

    result = json.load(f)
    print(type(result),result)
    print(result.get('name'))
    print(result.get('age'))
    print(result.get('address').get('city'))
    pass

