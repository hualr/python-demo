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

    print("finish init demo")


# 增删改
def update_dict():
    print("update dict demo")
    p = dict(a=1, b=2, c=3)

    # 删除
    p.pop("a")
    print(p)

    # 增加
    p['m'] = 'm'
    print(p)

    # 改
    p['m'] = 'n'
    print(p)

    # 批量添加
    u = dict(d=4, e=5)
    p.update(u)
    print(p)

    print("finish update dict demo")


# []和get的区别在于 []会报错
def visit_value():
    print("visit value demo")
    p = dict(a=1, b=2, c=3)
    print(p['a'])

    print(p.get('a'))
    print("visit value demo finish")

    print(p.get('k'))
    print(p.get('k', 'u'))
    # print(p['k'])


def remove():
    a = {1: 2, 3: 4, 5: 6}
    del a[1]
    print(a)
    # del a[6]
    print(a)
    # a_pop = a.pop(6)
    print(a)


if __name__ == '__main__':
    # init_dict()
    # update_dict()
    # visit_value()
    remove()
