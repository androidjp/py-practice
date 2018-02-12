import numpy as np

print('===================================')
print('[各种运算，生成新的矩阵]')
print('------')
a = np.array([10, 30, 40, 50])
b = np.arange(4)
c = a - b
print(c)

print(b ** 2)

print(10 * np.sin(a))

print(a < 35)

print('===================================')
print('[矩阵乘法 和 矩阵对应位置中元素的相乘不同]')
print('------')

a = np.array([[1, 1],
              [0, 1]])
b = np.array([[2, 0],
              [3, 4]])
print('只是对应位置相乘：\n', a * b)
print('矩阵乘法：\n', np.dot(a, b))
print('矩阵乘法(方式二)：\n', a.dot(b))

# += *= 是更新本矩阵，而不是新建矩阵

print('===================================')
print('[做了矩阵运算之后，矩阵中的元素type 的变化趋势：（int->float64->complex128）]')
print('------')

a = np.ones(3, dtype=np.int32)
b = np.linspace(0, np.pi, 3)
print(a, a.dtype.name)
print(b, b.dtype.name)
c = a * b
print(c, c.dtype.name)
# 转 复数
d = np.exp(c * 1j)
print(d, d.dtype.name)

print('===================================')
print('[取矩阵的最大最小值（忽略了行列的，直接把矩阵当一维数组）]')
print('------')

a = np.random.random((2, 3))
print(a)
print('sum:', np.sum(a))
print('max:', np.max(a))
print('min:', np.min(a))

print('===================================')
print('[用 axis 来做行列相关的一些矩阵统计]')
print('------')

a = np.arange(12).reshape(3, 4)
print(a)
print('每一列元素相加的结果，生成一个一维数据返回：\n', np.sum(a, axis=0))
print('每一行元素相加的结果，生成一个一维数据返回：\n', np.sum(a, axis=1))
print('每一行取一个最小值：\n', np.min(a, axis=1))
print('给矩阵的每一个坐标位置，都做了一个同一行元素累加的操作：\n', np.cumsum(a, axis=1))

print('===================================')
print('[numpy 中的通用函数（记为ufunc）,如：sin,cos,exp等]')
print('------')

b = np.arange(4)
print(b)
print('e的n次方（e 约等于  2.718281）：', np.exp(b))
print('开根：', np.sqrt(b))
print('次方根：', b**3)

print('===================================')
print('[索引,切片与迭代]')
print('------')
