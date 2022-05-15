# 读取完整文件
"""
第一个参数表示的是文件路径
第二个参数表示的是权限 r表示的是默认读取 w是写 b是以二进制打开 b没用的
第三个是编码方式
"""
file = "test.txt"
print("-----------读取完整文件-------------------")
with open(file, 'r', encoding='utf-8') as f:
    text1 = f.read()
    print(text1)

print("-----------一行一行读取文件-------------------")
with open(file, 'r', encoding='utf-8') as f:
    text2 = f.readline()
    print(text2)

print("-------------进阶使用----------------")
with open(file, 'r', encoding='utf-8') as f:
    text3 = ''
    line = f.readline()
    while line:
        text3 += line
        line = f.readline()
        print(line)

print(text3)
