# 局部导入 不需要写包
from os import getcwd
print(getcwd())

# 非局部导入必须写包
import os
print(os.getenv("with"))

from os import getgid as get_t

def getgid():
    print("我自己的gid方法")
# 重新命名了 as 所以不会存在冲突
print(get_t())
print(getgid())
