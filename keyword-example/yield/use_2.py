def gen_list():
    # 多个逻辑块 组成生成一个列表
    result = []
    for i in range(10):
        result.append(i)
    for j in range(5):
        result.append(j * j)
    for k in [100, 200, 300]:
        result.append(k)
    return result


for item in gen_list():
    print(item)


def gen_list2():
    # 多个逻辑块 使用yield 生成一个列表
    for i in range(10):
        yield i
    for j in range(5):
        yield j * j
    for k in [100, 200, 300]:
        yield k


for item in gen_list2():
    print(item)
