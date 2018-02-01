print('===================================')
print('[遍历对象内容]')
print('------')

ming = {
    'name': 'Ming',
    "age": 18,
    'level': None,
    'sex': True
}
for i in ming:
    print(i, ming[i])

print('===================================')
print('[遍历方式二]')
print('------')

for key,val in ming.items():
    print(key,val)