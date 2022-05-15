def list_arg(*arg):
    a = list(arg)
    print(a, type(a))


# 初始化
if __name__ == '__main__':
    my_list = [1, 2, 3, 4]
    print(my_list, type(my_list))

    # 只能这样和函数结合在一起
    list_arg(1, '2', 'e')
