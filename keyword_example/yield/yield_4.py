def fun1(n):
    i = 0
    while i < n:
        # return的结果
        temp = yield i
        i += 1
        print("temp:", temp)
        print("i:", i)


generate1 = fun1(4)

# 这种方式也是可用的
for i in generate1:
    print("return:", i)
