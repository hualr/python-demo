class A:
    # 就是static变量
    val1 = 1

    def __init__(self, val1=5):
        self.val1 = val1
        self.val2 = val1


# 这样定义一个类 有什么意义呢

if __name__ == '__main__':
    a = A()
    # 属性就算不存在也可以以临时变量的形式存在着
    a.i = 6
    a.j = 8
    print(a.i + a.j)

    # 这里修改了对象的val1
    print(a.val1)
    # 但是没有修改类的val1
    print(A.val1)
    print(a.val2)

    # 类的变量修改
    A.val1 = 6
    b = A()
    print(a.val1)
    print(b.val1)
    print(A.val1)
