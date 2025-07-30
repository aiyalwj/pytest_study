# fighting AX
# 2025/5/11 19:20
import requests

proxies = {
  'http': 'http://127.0.0.1:8888',
  'https': 'http://127.0.0.1:8888',
}
# response = requests.get('https://www.baidu.com/s?wd=iphone&rsv_spt=1')
# print(response.text)

urlpara = {
    'wd':'iphone&ipad',
    'rsv_spt':'1'
}

response = requests.get('http://www.baidu.com/s',params=urlpara,proxies=proxies)
print(response.text)