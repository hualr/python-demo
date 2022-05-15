a = [1, 2]
b = [1]

b.append(2)

# is比较的是地址 也就是id方法
print(a is b)
print(id(a) == id(b))

# ==比较的是值 也就是eq方法
print(a == b)
print(a.__eq__(b))
