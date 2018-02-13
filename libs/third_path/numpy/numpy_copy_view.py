import numpy as np

a = np.arange(12)
b = a
print(b is a)

b.shape = 3, 4

print(a.shape)

print('a 的 唯一标识：\n', id(a))
print('b 的 唯一标识：\n', id(b))
c = np.zeros_like(a)
print('c 的 唯一标识：\n', id(c))

print('===================================')
print('[View or 浅拷贝]')
print('------')

a = np.arange(12).reshape(2, 6)
c = a.view()
print('c是 a.view()生成的\n', c)
print('这时，c不等于a了\n', c is a)
print('但是c的data 是属于a的，c只不过是一个窗口而已\n', c.base is a)
print('c问自己,我的数据是属于我的吗？\n', c.flags.owndata)
c.shape = 3, 4
print('c调整了shape 为 3,4\n', c.shape)
print('但是a的shape并没有变\n', a.shape)
c[0, 0] = 1234
print('但如果c想update data 的话,是可以的\n', c)
print('a\n', a)

print('===================================')
print('[深拷贝]')
print('------')

a = np.arange(12).reshape(2, 6)
d = a.copy()
print('d不是与a指向同一个内存空间\n', d is a, d.base is a)
d[0, 0] = 99  # 这时 a 值不变

print('===================================')
print('[Functions / Methods ]')
print('------')

