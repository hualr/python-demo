# 构建了一个生成器
def fun1(n):
    i = 0
    while i < n:
        # return的结果
        yield
        i += 1
        print(i)


# 打印的是生成器的地址 这里开始 就构建了一个生成器
generate1 = fun1(4)
# 打印生成器的地址 这里才是第一个生成器
print(generate1)

print(next(generate1))
print(next(generate1))
# 当没有下一个 就直接出现stop异常了
print(next(generate1))
print(next(generate1))


'''
next方法就是迭代器内置的_next_
'''


