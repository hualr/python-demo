# hash是提取特征值 此时注意到! 可变对象无法处理
if __name__ == '__main__':
    m = 1234556
    print(hash(m))

    print("---")

    print(hash("Traditional"))

    print("---")

    print(hash((1, 2, 3, 4)))

    # list
    print(hash([1, 2]))
