# 返回原组
def test_new():
    name = "pythoneer"
    address = "cnblogs"
    # 推荐不写括号
    return name, address


print(test_new, type(test_new))
