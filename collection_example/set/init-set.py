# 初始化
print("-----------一行一行读取文件-------------------")
emptySet = set()
print(emptySet)

# 传参
dataScientist = set(['Python', 'R', 'SQL', 'Git', 'Tableau', 'SAS'])
print(dataScientist)
dataScientist = set(['A', 'A', 'A', 'B', 'B', 'B'])
# 默认去重
print(dataScientist)

# 增删确定存在性
# 注意到这个是Object
emptySet.add('1')
emptySet.add(2)
print(emptySet)

# 如果这个值不存在 remove报错 后者不报错
print(emptySet.remove(2))
print(emptySet.discard(2))
print(emptySet)

print(emptySet.__contains__('1'))

print("------------------迭代----------------------")
# 迭代
for a in dataScientist:
    print(a)

