import numpy as np

print('===================================')
print('[ravel(), reshape(), T  这三者都会返回一个新的矩阵]')
print('------')

a = np.arange(10).reshape(2, 5)
print(a)
print('ravel()\n', a.ravel())
print('reshape()\n', a.reshape(1, 10))
print('T\n', a.T)

print('===================================')
print('[resize() 又是什么鬼？]')
print('------')

a = np.arange(12)
print(a)
a.resize((2, 6))
print('resize() 之后\n', a)
print('reshape(有负数),自动判别\n', a.reshape((4, -1)))

print('===================================')
print('[多个数组，拼合]')
print('------')

a = np.floor(10 * np.random.random((2, 2)))
print('a\n', a)
b = np.floor(10 * np.random.random((2, 2)))
print('b\n', b)
c = np.vstack((a, b))
print('vstack(数组后面连接,2x2 -> 4x2)\n', c)
d = np.hstack((a, b))
print('hstack(每行左右拼接,2x2 -> 2x4)\n', d)

from numpy import newaxis

# column_stack is equivalent to hstack only for 2D arrays.
a = np.array([1, 2])
b = np.array([3, 4])
e = np.column_stack((a, b))
print('组成2D数组\n', e)
print('用hstack结果则不同\n', np.hstack((a, b)))
print(a[:, newaxis])

# row_stack is equivalent to vstack for any input arrays.

print('===================================')
print('[r_[...] 与 c_[...] 来构造数组]')
print('------')

print('打横拼矩阵\n', np.r_[0, 4, 1:4])
print('打竖拼矩阵\n', np.c_[np.array([1, 2, 3]), np.array([4, 5, 6])])

print('===================================')
print('[切分一个数组到若干个小数组]')
print('------')

a = np.arange(12).reshape(3, 4)
# a = np.floor(10 * np.random.random((2, 12)))
print('a\n', a)
b = np.hsplit(a, 2)
print('np.hsplit(a,3)之后：\n', b)

a.resize((2, 6))
print('a\n', a)
c = np.hsplit(a, (1, 2))
print('从第一列后边切下一竖,第二列右边切下一束,如此来分：\n', c)
