# 定义一个属性被删除后的行为+删除类属性
class MyClass:
    num = 1

    def __init__(self, work, score):
        self.work = work
        self.score = score

    def __delattr__(self, name):
        print("你正在删除一个属性")
        return super().__delattr__(name)


if __name__ == '__main__':
    test = MyClass(work="math", score=100)

    # 删除work属性
    del test.work

    # work属性删除,score属性还在
    print(test.score)

    try:
        print(test.work)
    except AttributeError as reason:
        print(reason)

    print(MyClass.num)
    delattr(MyClass, "num")
    print(MyClass.num)
