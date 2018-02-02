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

print('===================================')
print('[元组：tuple]')
print('------')

tupleA = (123, 'ABC')
print(tupleA)
