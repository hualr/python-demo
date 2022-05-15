# 我们注意到,初始化的时候a就是a 而非m
# ps 我感觉最有用的就是第一个
def init_dict():
    print("init dict demo")

    j = {'a': 1, 'b': 2}
    print(j)
    # 直接初始化
    a = "m"
    b = "n"
    c = 'z'
    p = dict(a=1, b=2, c=3)
    print(p)

    # 字典推导式
    f = {i: 2 + i for i in range(1, 5)}
    print(f)

    e = dict(zip('ab', [1, 2]))
    print(e)

    # fromKeys方式
    g = dict.fromkeys(range(5), 'v')
    print(g)

    keys = (1, 2, 3, 4)
    value = ('a', 'b', 'c')
    my_dict = dict.fromkeys(keys, value)
    print(my_dict)
    my_dict = dict.fromkeys(keys)
    print(my_dict)

    print("finish init demo")


init_dict()
