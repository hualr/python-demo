# 过滤出来奇数
res = filter((lambda x: x % 2 == 1), [1, 5, 6, 8])

# 转换成列表
res_list = list(res)
# 查看
print(res_list)

# map映射   将序列中的每一个元素作为 函数的参数 进行处理
res = map(lambda x: x * 2, [1, 2, 3, 4])
# 转换成列表
res_list = list(res)
# 查看
print(res_list)

# 整合

a = [1, 5, 6, 8]
m = map(lambda x: x * 2, filter((lambda x: x % 2 == 1), a))
n = filter((lambda x: x % 2 == 1), map(lambda x: x * 2, a))
print(list(m))
print(list(n))
