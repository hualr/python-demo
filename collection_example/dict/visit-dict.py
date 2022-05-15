# []和get的区别在于 []会报错
def visit_value():
    print("visit value demo")
    p = dict(a=1, b=2, c=3)
    print(p['a'])

    print(p.get('a'))
    print("visit value demo finish")

    print(p.get('k'))
    # getOrDefault
    print(p.get('k', 'u'))
    # print(p['k'])

    print(p.values())
    for i in p.values():
        print(i)

    for k, v in p.items():
        print('key=', k, ',', 'value=', v)

    for item in p.items():
        print('key=', item[0], ',', 'value=', item[1])

    # 这里默认是比较p.keys的迭代
    print(1 in p)
    print('a' in p)


visit_value()
