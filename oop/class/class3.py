class A:
    def __init__(self):
        print("hello wolrd")


# B继承了A
class B(A):
    def __init__(self):
        # 如果不去调用 那么是无法继承到A的构造器的
        # super().__init__()
        print("hello")

# 构造器的继承是无法自动继承的
b = B()
