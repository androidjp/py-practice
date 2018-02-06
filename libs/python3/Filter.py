print('===================================')
print('[filter() 过滤序列]')
print('--------------')


def func_filter(x):
    return True if x % 3 == 0 else False


L = list(filter(func_filter, [1, 2, 3, 4, 5, 6]))
print(L)

L2 = list(filter(lambda x: x and x.strip(), ['A', '', 'B', '  ', 'C']))
print(L2)

print('===================================')
print('[筛选函数的定义]')
print('--------------')


def _odd_iter():
    n = 1
    while True:
        n += 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()  # 初始序列
    while True:
        n = next(it)  # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it)  # 构造新序列


# 打印1000以内的素数:
for n in primes():
    if n < 20:
        print(n)
    else:
        break
