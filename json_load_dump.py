# fighting AX
# 2025/5/23 13:20
import json

'''
json.loads(s, *, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)
将 JSON 字符串转换为 Python 对象(dict)
    其中，s 是 JSON 格式的字符串。
    
        注意：json.load()是从文件中读取JSON数据 json.loads()是从JSON字符串中读取数据
'''
str1 = '{"name": "John", "age": 30, "city": "New York"}'
load_str1 = json.loads(str1)
print(type(load_str1))
print(load_str1)

'''
json.dumps(obj, *, skipkeys=False, ensure_ascii=True, check_circular=True,
        allow_nan=True, cls=None, indent=None, separators=None,
        default=None, sort_keys=False, **kw)
将 Python 对象(dict) 转换为 JSON 字符串
    其中，obj 是要转换的 Python 对象，其他参数用于控制转换过程中的各种选项。
'''

data = {
    "name": "John",
    "age": 3,
    "city": "New York"
}

dump_data = json.dumps(data)
print(type(dump_data))
print(dump_data)