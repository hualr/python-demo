# 其实就是省略了一个def而已
def main1():
    g = lambda x, y: x + y

    var = g(2, 3)
    print(var)


if __name__ == '__main__':
    main1()
