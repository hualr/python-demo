# 全局变量无法被def函数修改 除非函数中说明
gl_name = "hello world"


# 定义一个函数，尝试修改全局变量
def change1():
    # 在函数内部不允许直接修改全局变量的引用
    # 那么这里的gl_name是什么呢？
    # 局部变量！
    # 这种特性是为了限制 全局变量 的可变范围。许多程序需要约束。
    gl_name = "ok"


def change2():
    global gl_name
    gl_name = "ok"


if __name__ == '__main__':
    change1()
    print(gl_name)
    change2()
    print(gl_name)
