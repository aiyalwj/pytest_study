# fighting AX
# 2025/5/5 19:56
try:
    #可能发生异常的代码
    pass
# except 异常类型1:
#     #发生其他类型的异常会执行的代码
#     pass
# except 异常类型2:
#     # 发生其他类型的异常会执行的代码
#     pass
except Exception as 变量:
    pass
else:
    #没有发生异常会执行的代码
    pass
finally:
    #不管有没有发生异常，都会执行的代码
    pass

if __name__ == '__main__':
    print('hello')