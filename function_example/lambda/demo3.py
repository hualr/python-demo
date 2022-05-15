# 内嵌函数

def my_fun():
    # 内嵌函数 或者 内部函数 的关键在于访问内嵌函数的权限问题
    print('外部函数')

    # 注意命名格式
    def inner_fun_fun():
        print('内嵌在MyFun中的函数,只能在MyFun函数中被调用')

    # 缩进格式的对其，差一个空格 都不行
    inner_fun_fun()


if __name__ == '__main__':
    my_fun()
