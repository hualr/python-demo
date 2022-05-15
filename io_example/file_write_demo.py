import pickle

if __name__ == '__main__':
    # 要存储的列表
    my_list = [321, 654, 987, '行初心']

    # 将列表保存在这个文件中,文件的后缀名可以任意，因为起到的是提示作用
    # wb 写入 二进制
    # 将列表写入文件
    with open("my_list.txt", 'wb') as f:
        pickle.dump(my_list, f)
    # 缩进还真不是可以随意的

    # 以二进制的方式读取
    with open('my_list.txt', 'rb') as f:
        my_new_list = pickle.load(f)

    # 一定要注意 要写关闭文件
    print(my_new_list)
