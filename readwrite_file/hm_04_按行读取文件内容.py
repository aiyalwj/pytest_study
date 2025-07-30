# fighting AX
# 2025/5/5 19:28
with open('a.txt', 'r', encoding='utf-8') as f:
    # buf = f.readline()
    # print(buf)
    # print(f.readline())

    for i in f:
        # print(i)
        print(i,end='')


print("\n")
with open('a.txt', 'r', encoding='utf-8') as f1:
    while True:
        buf = f1.readline()
        if len(buf) == 0 :
            break
        else:
            print(buf,end='')