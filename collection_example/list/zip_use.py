# 我真觉得没啥用
from itertools import zip_longest

if __name__ == '__main__':
    a = [1, 2, 3]
    b = ['a', 'b', 'c', 4]

    for x, y in zip(a, b):
        print(x, y)

    for x, y in list(zip(a, b)):
        print(x, y)

    print('结束展示1')
    for x, y in zip(b, a):
        print(x, y)

    print('默认匹配到短的')

    for x, y in zip_longest(a, b):
        print(x, y)

    print('补全长的')
