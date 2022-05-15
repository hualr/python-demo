def my_abs(x):
    # 类型判断
    if not isinstance(x, (int, float, bool)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


def mytest(a, b):
    print(a)
    print(b)


if __name__ == '__main__':
    print(my_abs(-1))
    # 不按照顺序来
    mytest(b="nihao", a="万岁")
