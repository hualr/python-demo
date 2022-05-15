# id其实就是在看某个对象的引用
if __name__ == '__main__':
    a = 1
    b = a
    print(id(a))
    print(id(b))
    a = 2
    print(id(a))
    print(id(b))
