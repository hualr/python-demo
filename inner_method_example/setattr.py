# 设置属性的时候需要新增的提示功能+ 新增类属性
class MyClass:
    def __init__(self, work):
        # 这里就在设置 私有属性work的值
        self.work = work

    def __setattr__(self, name, value):
        print("你正在设置一个存在的属性的值")
        return super().__setattr__(name, value)


if __name__ == '__main__':
    MyClass(work="coding")
    # ！！！点题一句--->利用setattr进行创建属性
    setattr(MyClass, 'name', "xingchuxin")

    # 查看效果
    print(getattr(MyClass, 'name', "introduction"))
