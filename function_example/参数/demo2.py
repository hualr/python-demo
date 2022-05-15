# 默认参数说明

# 如果不赋值 那么就是默认写的
def move(x, y, angle=0):
    nx = x
    ny = y
    na = angle
    return nx, ny, na


# 默认参数不能为list 因为list可变
def add_end1(my_list=None):
    if my_list is None:
        my_list = []
    my_list.append('END')
    return my_list


if __name__ == '__main__':
    print(move(1, 2))
    print(move(1, 2, 3))

    print(add_end1())
    print(add_end1([1, 2, 3]))

