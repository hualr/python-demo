class Father:
    pass


class Son(Father):
    pass


class GrandSon(Son):
    pass


class MyClass:
    pass


def main():
    test = GrandSon()
    # 判断前者是否是后者的一个实例化对象

    print(isinstance(test, GrandSon))
    # 连基类也是
    print(isinstance(test, Father))

    # 也可以使用元组，有一个是就是
    print(isinstance(test, (GrandSon, MyClass)))


if __name__ == '__main__':
    main()
