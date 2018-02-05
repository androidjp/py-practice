print('===================================')
print('[一个数组可以扔各种类型的东西进来]')
print('------')

arr = [];
arr.append(1)
arr.append('A')
arr.append({
    'name': 'Ming',
    "age": 18,
    'level': None,
    'sex': True
})
print(arr)

print('===================================')
print('[数组遍历]')
print('------')

students = [
    {
        'name': 'Ming',
        "age": 18,
        'level': None,
        'sex': True
    },
    {
        'name': 'Fang',
        "age": 17,
        'level': None,
        'sex': False
    }
]
print(students)
for item in students:
    for key, val in item.items():
        print('%s --> %s' % (key, val))

print('===================================')
print('[数组遍历方法二]')
print('------')

for index, stu in enumerate(students):
    print(index)
    for i, field in enumerate(stu):
        print(i, field)

print('===================================')
print('[集合：Set]')
print('------')

setA = {123, 'ABC'}
print(setA)
setB = set([1, 1, 2, 3, 3])
print(setB)

print('===================================')
print('[元组：tuple]')
print('------')

tupleA = (123, 'ABC')
print(tupleA)

print('===================================')
print('[dict 字典 --> 相当于 Map : 无序，存取速度快，但是很耗内存]')
print('--------------')

dictA = {'Bob': 18, 'Amy': 28}
print(dictA['Amy'])
print('Tom' in dictA)
dictA['Tom'] = 'Leader'
print('Tom' in dictA)
print(dictA['Tom'])

print('===================================')
print('[dict 的遍历]')
print('--------------')

dictB = {'A': 'BA', 'B': 'DEV', 'C': 'manager'}
for key in dictB:
    print('key', key)

for val in dictB.values():
    print('value', val)

for k, v in dictB.items():
    print(k, v)

print('===================================')
print('[如何快速生成number数组]')
print('--------------')

print('1到10的数组', list(range(1, 10)))
setNumA = {x * x for x in range(1, 31) if x % 5 == 0}
print('1到30的5的倍数的数的2次方数集合', setNumA)
print('两层循环全排序：', [m + n for m in 'ABC' for n in '12'])

print('===================================')
print('[数组中的元素全部转成小写]')
print('--------------')

s = ['A', 'B', 'C']
print([item.lower() for item in s])
