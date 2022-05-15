def consumer():
    i = None
    while True:
        # 拿到 producer 发来的数据
        j = yield i
        print('consume %s' % j)


def producer(c):
    next(c)
    for i in range(5):
        print('produce %s' % i)
        # 发数据给 consumer
        c.send(i)
    c.close()


c = consumer()
producer(c)

'''
1. 首先消费者生成一个实际的迭代器
2. 调用生产者方法 此时生产者关联着消费者
3. 第一次调用next方法 此时程序走到第一次的yield
4. 开始调用send 每次调用一次send后 j拿到值 然后在下一次遇到yield后又开始停止
5. 继续往后走 周而复始
'''
