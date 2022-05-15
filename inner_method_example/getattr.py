# 定义访问不存在属性时的行为+ 类属性查询
class MyClass:

    num=0
    def __init__(self, work):
        self.work = work

    def __getattr__(self, name):
        """
            class MyClass  def __getattr__(self, name)
            Inferred type: (self: MyClass, name: Any) -> None
        """
        print("你正在访问一个不存在的属性")



if __name__ == '__main__':
    # 访问不存在的属性
    MyClass(work=1).not_exist_attr

    # 访问存在的属性
    MyClass(work=1).work

    print(getattr(MyClass, "num", "属性不存在"))
    print(getattr(MyClass, "num1", "属性不存在"))
