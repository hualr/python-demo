def check(func):
    print("正在检测权限")
    func()


def get_name():
    print("get_name_func")


def get_name2(name="太阳"):
    print(name)


if __name__ == '__main__':
    check(get_name)
    check(get_name2)
    check(get_name2("月光"))
