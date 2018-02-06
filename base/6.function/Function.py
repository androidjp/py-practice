print('===================================')
print('[python 写函数的特别之处：]')
print('------')

print('===================================')
print('[指定传入参数的默认值]')
print('------')

print('===================================')
print('[可变参数]')
print('------')


def mthd(id, *params):
    print('id: ', str(id))
    print(params)


mthd(11)
mthd(11, 'xiaoming', True)

print('===================================')
print('[指定可变参数们的名称]')
print('------')


def mthd(id, *, job):
    print('id: ', str(id))
    print(job)
    pass


mthd(123, job='EN')

print('===================================')
print('[传入一个dict]')
print('------')


def mthd(name, **msg):
    print(name)
    for key, val in msg.items():
        print(key, val)


mthd('ming', msg={'age': 18, 'major': 'English'})
