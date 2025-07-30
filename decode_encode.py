# fighting AX
# 2025/5/23 12:35

'''
string.encode(encoding, errors)
将字符串 转换为 指定编码格式的字节序列 string -> bytes
    其中，encoding参数指定的编码格式，例如UTF-8、GBK等
        errors是可选参数，用于指定编码错误的处理方式
'''
str1 = 'hello你好！'
encode_str1 = str1.encode(encoding='utf-8')
print(type(encode_str1))
print(encode_str1)

'''
bytes.decode(encoding, errors)
将字节序列 解码为 指定编码格式的字符串 bytes -> string
'''
decode_str1 = encode_str1.decode('utf-8')
print(type(decode_str1))
print(decode_str1)
