a = []
a.append(1)
a.append("2")
print(a)

a.pop(0)
print(a)

a.remove("2")
print(a)

b = ['1', '2']
b.insert(1, 3)
print(b)

b.insert(len(b), [1, 2, 3, 4])
print(b)

x = [1, 2, 3]
y = ['1', '2', '3']
# addAll
x.extend(y)
print(x, y)
