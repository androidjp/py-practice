import numpy as np

print('===================================')
print('[生成一个零向量]')
print('------')

z = np.zeros((2, 3))
print(z)
print(type(z[0, 0]))

z2 = np.arange(15)
print(z2)
print(type(z2))
print('reshape之后：', z2.reshape(3, 5))

print(z2.dtype.name)
print(z2.itemsize)
print(z2.size)

b = np.array([-1, -2, -3])
print(b)

