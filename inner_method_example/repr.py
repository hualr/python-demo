# 如果str存在 打印str 否则打印__repr__
class MyClass:
    # def __str__(self):
    #     return "MyClass__str__"

    def __repr__(self):
        return "MyClass__repr__"


if __name__ == '__main__':
    print(MyClass)
    test = MyClass()
    print(test)
