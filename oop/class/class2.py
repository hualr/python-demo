# 1. 类中的方法都是需要引入self
# 2. 类中的构造器只能存在一个
# 3. 在构造器中定义成员变量

class A:
    """
    构造器的属性
    1. 构造器的属性 一定需要用self 否则就是局部变量了
    2. 构造器不支持重载 也就是说 一个类只允许存在一个构造器 后者会覆盖前者
    """

    # def __init__(self):
    #     # 构造器中的属性 必须用self
    #     self.i = 9

    def __init__(self, other):
        self.other = other


# 这里就是定义了一个list
class B:
    def __init__(self, score1, score2, score3):
        self.scores = [score1, score2, score3]


if __name__ == '__main__':
    a = A(7)
    print(a.other)
    stu_1 = B(80, 90, 85)
    print(stu_1.scores)
