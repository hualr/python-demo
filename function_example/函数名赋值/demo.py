def a():
    print("hello world")


a()

# 不写()不会被运行
print(a)
print(type(a))

b = a
b()
