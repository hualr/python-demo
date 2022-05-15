emptySet = set()
# 增删确定存在性
# 注意到这个是Object
emptySet.add('1')
emptySet.add(2)
print(emptySet)

# 如果这个值不存在 remove报错 后者不报错
print(emptySet.remove(2))
print(emptySet.discard(2))
print(emptySet)

print('1' in emptySet)
