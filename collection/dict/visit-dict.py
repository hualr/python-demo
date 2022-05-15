
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

