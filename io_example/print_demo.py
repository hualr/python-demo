# python基本函数
# 一. 基本输入输出
print("基本函数")
print('a', 'b')
print('a', 'b', sep='*')

word1 = 'hello'
word2 = 'hello'
# 用% 作为占位符
print("word1 == word2:%s" % (word1 == word2))

word3 = "hello"

# 三个引号可以表示换行处理 但是真的会这样用吗
word5 = '''hel
lo'''
print("word5:%s" % word5)

# 下面是换行不生效

word6 = "hello" \
        "world"
print("word6:%s", word6)

# 这个用的多
name = 'jane'
print(f'Hi,{name}')

w = 2
print('%.2f' % w)
print(f'w = {w:.2f}')
