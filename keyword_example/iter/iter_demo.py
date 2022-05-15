mylist = iter(["apple", "banana", "cherry"])
print(next(mylist))

print(next(mylist))

print(next(mylist))

# 走不下去就用橙子补
print(next(mylist, "orange"))

print(next(mylist, "orange"))
