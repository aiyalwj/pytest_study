# fighting AX
# 2025/5/5 19:39
'''
写入json文件
    1.导包import json
    2.写打开文件
    3.写入
    json.dump(数据类型,文件对象)
返回的是 字典（文件中是对象）或者列表（文件中是数组）
'''
import json
my_list = [('admin','123456','登录成功'),('root','123456','登录成功'),('admin','123123','登录失败')]
with open('info1.json', 'w', encoding='utf-8') as f:
    # json.dump(my_list,f)
    # json.dump(my_list,f,ensure_ascii=False) #直接显示中文，不以ASCII方式显示
    json.dump(my_list,f,ensure_ascii=False,indent=2) #显示缩进