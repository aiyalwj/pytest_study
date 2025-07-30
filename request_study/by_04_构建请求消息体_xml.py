# fighting AX
# 2025/5/11 19:20
import requests

payload = '''
<?xml version="1.0" encoding="UTF-8"?>
<WorkReport>
    <Overall>良好</Overall>
    <Progress>30%</Progress>
    <Problems>暂无</Problems>
</WorkReport>
'''

proxies = {
  'http': 'http://127.0.0.1:8888',
  'https': 'http://127.0.0.1:8888',
}

# 上面的例子里面包含中文，不能用缺省 latin-1编码.
# 所以我们将字符串对象，用 utf8 编码为字节串对象Bytes 传入给data参数，Requests就会直接把这个字符串放到 http消息体中，发送出去。
response = requests.get('http://www.baidu.com/s',
                        data=payload.encode('utf-8'),
                        proxies=proxies)
print(response.text)