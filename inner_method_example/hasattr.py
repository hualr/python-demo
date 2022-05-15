class MyClass:
    # 类属性
    num = 1


def main():
    # 属性的名字是字符串
    print(hasattr(MyClass, 'num'))
    print(hasattr(MyClass, 'n'))


if __name__ == '__main__':
    main()
