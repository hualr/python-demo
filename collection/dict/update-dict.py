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



update_dict()