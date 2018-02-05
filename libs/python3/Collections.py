from collections import Iterable

print('===================================')
print('[collections.Iterable 判断一个对象是否可被遍历]')
print('--------------')

print(isinstance('abc', Iterable))
print(isinstance(123, Iterable))
print(isinstance({1, 2, 3}, Iterable))

