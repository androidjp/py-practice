import itertools

print('===================================')
print('[无限迭代器]')
print('------')

d = itertools.count(1)
c = itertools.cycle(['a', 1, 'B'])

print('===================================')
print('[指定重复次数的迭代]')
print('------')

r = itertools.repeat(['a', 1, 'B'], 3)
for item in r:
    print(item)

print('===================================')
print('[创建一个迭代对象，从无限迭代器中截取一部分数据]')
print('------')

# 一旦判断条件filter 为 False , 截取就停止
p = itertools.takewhile(lambda x: x <= 10, d)
print(list(p))

print('===================================')
print('[chain 合并迭代器]')
print('------')

for i in itertools.chain('123', 'ABC'):
    print(i)

print('===================================')
print('[groupby 将迭代器中相邻的相同元素group起来]')
print('------')

for key, group in itertools.groupby('AaBBbCCAAA', lambda x: x.lower()):
    print(key, list(group))
