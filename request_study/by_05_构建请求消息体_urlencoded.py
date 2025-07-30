# fighting AX
# 2025/5/11 19:20
import requests

payload = {'key1': '你好', 'key2': 'urlencode'}

proxies = {
  'http': 'http://127.0.0.1:8888',
  'https': 'http://127.0.0.1:8888',
}

response = requests.get('http://www.baidu.com/s',
                        data=payload,
                        proxies=proxies)
print(response.text)