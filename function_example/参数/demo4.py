# 键值对参数

def demo_func(**kw):
    print(kw)


if __name__ == '__main__':
    demo_func(a=10, b=20, c=30)
