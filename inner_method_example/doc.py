# 获取方法的文档


def fun_single_doc(num):
    " 单行函数文档 "
    # pycharm会提示：使用 """ 代替 "
    return num + 1


def fun_multiple_doc():
    """
        多行的函数文档
        单行文档不好，推荐使用多行的函数文档。
        pycharm有快捷键ctrl+q，可以快捷查看函数的说明信息。
    """


if __name__ == '__main__':
    print(fun_single_doc.__doc__)
    print(fun_multiple_doc.__doc__)
