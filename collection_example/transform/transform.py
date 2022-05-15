test_list = list('test_str')
print(test_list)

my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
my_list = list(my_tuple)
print(my_list)

numbers = [1, 2, 3, 4, 5, 6]
print(numbers)

# 目的是生成索引加value的结构 不是map!

new_numbers = list(enumerate(numbers))

print(new_numbers)
