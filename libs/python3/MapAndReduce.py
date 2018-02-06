print('===================================')
print('[函数的运用：py自带的高阶函数：map()]')
print('------')


def f(x):
    return x * x


def convert2Str(num):
    return str(num)


# map(function , Iterable)
r = map(f, [1, 2, 3, 4, 5, 6])
print(r)  # 得到的r 是一个 惰性序列 Iterator
print(list(r))
print('利用map(), number 转 string: ', list(map(convert2Str, [1, 2, 3, 4, 5, 6])))

print('===================================')
print('[函数的运用：py自带的高阶函数：reduce()]')
print('------')

from functools import reduce


def add(a, b):
    return a + b


print(reduce(add, [1, 2, 3]))

print('===================================')
print('[reduce配合map 实现 int()]')
print('------')

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def char2Num(s):
    return DIGITS[s]


def str2int(s):
    return reduce(lambda a, b: a * 10 + b, map(char2Num, s))


num = str2int('43221')
print(num)
print(isinstance(num, str))
