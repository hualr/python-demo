class Father:
    pass


class Son(Father):
    pass


class GrandSon(Son):
    pass


class MyClass:
    pass


def main():
    print(issubclass(MyClass, object))

    print(issubclass(MyClass, GrandSon))

    print(issubclass(GrandSon, (Son, MyClass)))

    print(issubclass(MyClass, MyClass))


if __name__ == '__main__':
    main()
