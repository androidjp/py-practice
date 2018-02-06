print('===================================')
print('[各种类型转换函数]')
print('--------------')

s = '123'
print(int(s))
s = '12.23'
print(float(s))
print(str(112.22))
print(bool(1))
print(bool(''))

print('===================================')
print('[math 类库中的各种函数]')
print('--------------')

print('===================================')
print('[abs(x)]')
print('--------------')

a = -1
print(abs(a))

print('===================================')
print('[max(数组)]')
print('--------------')

print(max([1, 2, 3, 4, 8, 7, 6]))

print('===================================')
print('[各种三角函数(需要导入：math 包)]')
print('------')
import math

print(math.sin(math.pi))
print(math.sin(math.pi / 2))
print('sin(45度)： ', math.sin(45 * math.pi / 180))
print('cos(45度)： ', math.cos(45 * math.pi / 180))
