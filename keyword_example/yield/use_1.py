# 一次性生成返回
def big_list1():
    result = []
    for i in range(10000000000):
        result.append(i)
    return result


# for i in big_list1():
#     print(i)


# 要杀生成啥 局部返回
def big_list2():
    for i in range(10000000000):
        yield i


for i in big_list2():
    print(i)
