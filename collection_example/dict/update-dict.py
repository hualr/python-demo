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


    my_dict = {'子': '鼠', '丑': '牛', '寅': '虎',
               '卯': '兔', '辰': '龙', '巳': '蛇',
               '午': '马', '未': '羊', '申': '猴',
               '酉': '鸡', '戌': '狗', '亥': '猪'}

    # 如果找不到，就会添加. 当存在 那么无效
    # 显然键 '子'存在，那么 值 '属鼠' 也就无用 发返回的是原本的key
    print(my_dict.setdefault('子', '属鼠'))

    # 找得到返回 返回的是原本的key
    print(my_dict.setdefault('子'))

    # 如果找不到，就会添加. 返回的是即将添加的key
    print(my_dict.setdefault('行初心', '博客园'))
    print(my_dict)

    # 不存在的键"行"，未指定值，默认返回None value为none
    print(my_dict.setdefault('行'))


update_dict()
