import numpy as np

print('===================================')
print('[读写.npy文件]')
print('------')

np.save('./data', np.array([[1, 2, 3], [4, 5, 6]]))
res = np.load('./data.npy')
print(res)

# 用memap 去当做“cursor” 去读你想读取的文件内容位置
x = np.load('data.npy', mmap_mode='r')
print('读第二行数据：', x[1, :])

print('===================================')
print('[读写npz 文件]')
print('------')
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([1, 2])
np.savez('./data2', a=a, b=b)

data = np.load('./data2.npz')
print('a', data['a'])
print('b', data['b'])
data.close()

# 用memap 去当做“cursor” 去读你想读取的文件内容位置
x = np.load('data2.npz', mmap_mode='r')
print('读a每一行的第3个数据：', x['a'][:, 2])
