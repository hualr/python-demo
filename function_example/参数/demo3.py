# 可变参数 和* 拆包

def calc(*numbers):
    my_sum = 0
    for n in numbers:
        my_sum = my_sum + n * n
    return my_sum


if __name__ == '__main__':
    print(calc(1, 2, 3, 4))
    # 如果是容器类型想要传入 那么必须 加入*
    print(calc(*(1, 2, 3, 4)))
    print(calc(*[1, 2, 3, 4]))
