# 异常的捕获
if __name__ == '__main__':
    try:
        sum1 = 1 + '1'  # 数据类型错误
        file = open('不存在的文件.txt')
        file.close()
        # 多个异常的捕获
    except (OSError, TypeError) as reason:
        print('错误的原因是:', str(reason))
    except ZeroDivisionError as reason:
        print('数据类型错误', '\n错误的原因是:', str(reason))


    try:
        # sum1=1+'1' #数据类型错误
        file = open('不存在的文件.txt')
        file.close()
    except:
        print('错误未知')

    try:
        raise OSError('手动指明的原因')
    except OSError as reason:
        print('异常', str(reason))
    else:
        # 无法执行到的代码
        print('程序无异常')
    finally:
        print('反正要执行到这里')
