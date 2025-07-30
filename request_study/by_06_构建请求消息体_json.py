# fighting AX
# 2025/5/11 19:20
import json

import requests

payload = {
    "Overall":"良好",
    "Progress":"30%",
    "Problems":[
        {
            "No" : 1,
            "desc": "问题1...."
        },
        {
            "No" : 2,
            "desc": "问题2...."
        },
    ]
}


proxies = {
  'http': 'http://127.0.0.1:8888',
  'https': 'http://127.0.0.1:8888',
}
# dumps编码 将 Python 对象序列化为 JSON 格式的字符串
response = requests.get('http://www.baidu.com/s',
                        data=json.dumps(payload,ensure_ascii=False),
                        proxies=proxies)
print(response.text)