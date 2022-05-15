# 通过定义参数 确定形参和实参

def mytest(a, b):
    print(a)
    print(b)


if __name__ == '__main__':
    # 不按照顺序来
    mytest(b="nihao", a="万岁")
