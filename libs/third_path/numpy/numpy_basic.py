import numpy as np

print('===================================')
print('[arange() 类似 for..in range() 中的range() ,作为一个整数数组生成器]')
print('------')

z2 = np.arange(15)
print(z2)
print(type(z2))
print('reshape之后：\n', z2.reshape(3, 5))

print('查看里面每个元素的类型：', z2.dtype.name)
print('查看每一行的元素个数', z2.itemsize)
print('查看所有元素总数', z2.size)

print('===================================')
print('[生成一个ndarray]')
print('------')

b = np.array([-1, -2, -3])
print(b)
print(type(b))

b = np.array([(1, 2, 3), (-1, 0, 5.8)])
print(b)
print(b.dtype.name)

# 数组元素类型也可以在 创建数组时， 给定
b = np.array([(1, 2), (3.3, 4.4)], dtype=complex)
print(b)
print(b.dtype.name)

print('===================================')
print('[zeros 生成数组,注意,每一个值都是float类型]')
print('------')
# 通常最开始,数组的元素值的不定的,但是数组的所占空间是可以确定的,所以有了这些np 的函数,去初始化数组。
z = np.zeros((2, 3))
print(z)
print(type(z[0, 0]))

print('===================================')
print('[ones 生成全一的数组，并规定元素类型]')
print('------')

arrOne = np.ones((2, 3, 4), dtype=np.int16)
print(arrOne)

print('===================================')
print('[empty 创建的数组将会尽他所能地得到足够的内存空间来创建内容，但默认的元素类型还是float64]')
print('------')

arrRandom = np.empty((2, 3))
print(arrRandom)

print('===================================')
print('[zeros_like()和 ones_like(),empty_like() 来copy数组格式]')
print('------')

print('zeros_like: ', np.zeros_like(([1, 2, 3], [4, 5, 6]), dtype=float))
print('ones_like: ', np.ones_like(([1, 2, 3], [4, 5, 6])))
print('empty_like: ', np.empty_like(([1, 2, 3], [4, 5, 6])))

print('===================================')
print('[arange(fromNum, toNum, 间隔)]')
print('------')

print(np.arange(10, 30, 5))
print('相当于：', np.array([10, 15, 12, 25]))
print('比Py自带的range厉害的是，还能获取float数组：', np.arange(0, 2, 0.3))

print('===================================')
print('[linespace(from, to(闭区间), 要分出多少个元素出来)]')
print('------')
# 2*pi，分9份，再转角度
x = np.linspace(0, 2 * np.pi, 9)
print('2*pi，分9份：', x)
print('转sin值：', np.sin(x))
for i in x:
    print(i * 180 / np.pi, '度')

print('===================================')
print('[reshape(分层1,...,分层n)]')
print('------')

print(np.arange(1, 100).reshape(3, 3, 11))

nn = np.arange(10000).reshape(100, 100)
print(nn)
print('打印不完全怎么办？np.set_printoptions()')
np.set_printoptions(threshold=np.nan)
# print(nn)

print('===================================')
print('[random 生成[0.0, 1.0)的浮点数]')
print('------')

print(np.random.random_sample(), '类型：', type(np.random.random_sample()))
print(np.random.random_sample((4,)))

print('分成3份，每份2个：\n', np.random.rand(3, 2))

print('一个浮点数：', np.random.randn())
print('或者，标准正态分布的一个样本结果：', 2.5 * np.random.randn(2, 4) + 3)

print('===================================')
print('[fromfunction(func, shape, **kwargs), 通过每一个坐标执行一个函数来生成一个数组]')
print('------')

print(np.fromfunction(lambda i, j: i == j, (3, 3), dtype=int))
print(np.fromfunction(lambda i, j: i + j, (3, 3), dtype=int))

