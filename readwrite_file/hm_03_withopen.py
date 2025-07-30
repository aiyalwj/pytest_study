# fighting AX
# 2025/5/5 19:22
'''
with opne(file,mode,encoding='utf-8') as 变量:
    #在缩进中去读取或写入文件

#缩进中的代码执行结束，出缩进之后，文件会自动关闭

>with open打开文件
    不用自己去书写关闭文件的代码，会自动进行关闭
'''

with open('a.txt', 'a', encoding='utf-8') as f:
    f.write('good good study')
    #a方式打开文件，文件不存在会创建文件，文件存在，在文件的末尾写入内容