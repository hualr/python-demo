def fun1(n):
    i = 0
    while i < n:
        # return的结果
        temp = yield i
        i += 1
        print(temp)
        print(i)


generate1 = fun1(4)
print(generate1)

# next和send的区别在于 send可以传值 但是返回的还是yield后面的结果
print(next(generate1))
print(generate1.send("hello world"))
print('============')
print(next(generate1))
