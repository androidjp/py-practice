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

print('===================================')
print('[一句英文，首字母转大写]')
print('--------------')

dialog = 'i was a body.'
res = reduce(lambda x, y: x + ' ' + y, map(lambda c: c[0].upper() + c[1:] if c[0].isalpha() else c, dialog.split()))
print(res)

print('===================================')
print('[对一个dict做filter ,把他内部所有_开头属性都filter掉]')
print('------')
# 第二种写法
# dic0 = {"_id":"123456", "_class":"class", "name":"yes"}
dic = dict(_id="123456", _class="class", name="yes")
print(isinstance(dic, object))
print('原来的dic\n', dic)

res = dic.copy()
for it in dic:
    if it == '_id':
        del res[it]
dic.clear()
print('filter之后的dic\n', res)
