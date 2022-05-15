# 其实就是函数式编程了
def fun_out(wai):
    # 1 对于fun_out,fun_inner是内部函数
    def fun_inner(nei):
        # 2 对在外部作用域（fun_out的整个函数空间）的变量（out）进行引用
        # 达到1 2两个要求，就说fun_inner是闭包
        return wai + nei

    return fun_inner  # 函数的名字也是一个对象，可以返回


temp = fun_out(2)
print(temp)

print(type(temp))

print(temp(3))  # 这个很有趣

# 感觉和C语言的指针很像呀
print(fun_out(2)(3))
