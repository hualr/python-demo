# 和上一个的区别在于yield的结果 就是return结果
def fun1(n):
    i = 0
    while i < n:
        # return的结果
        yield i
        i += 1
        print(i)


# 打印的是生成器的地址 这里开始 就构建了一个生成器
generate1 = fun1(4)
# 打印生成器的地址
print(generate1)

print(next(generate1))
print(next(generate1))
print(next(generate1))
print(next(generate1))
