from collections import Iterable, namedtuple, deque, defaultdict, OrderedDict, Counter

print('===================================')
print('[5.collections.Iterable 判断一个对象是否可被遍历]')
print('--------------')

print(isinstance('abc', Iterable))
print(isinstance(123, Iterable))
print(isinstance({1, 2, 3}, Iterable))

print('===================================')
print('[带有名字的元组 ： namedtuple]')
print('------')

Circle = namedtuple('Circle', ['x', 'y', 'r'])
c = Circle(1, 1, 9)
print(isinstance(c, Circle), isinstance(c, tuple))

print('===================================')
print('[双向列表（作用：队列和栈） --> deque]')
print('------')
q = deque([1, 2, 3])
q.popleft()
q.append(-1)
q.appendleft(10)
print(q)

print('===================================')
print('[key不存在，返回默认值--- defaultdict]')
print('------')
dd = defaultdict(lambda: 'N/A')
dd['name'] = 'Ming'
print(dd['name'], dd['age'])

print('===================================')
print('[有序的dict --- OrderedDict  (先进先出)]')
print('------')

od = OrderedDict()
od['z'] = 1
od['b'] = 2
od['c'] = 3
print(od)

print('===================================')
print('[统计字符个数 --- Counter]')
print('------')

c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1

print(c)
