from oo.year_end_award_system.model.Person import Person


# [获取对象类型]
def getObjType(obj):
    print(type(obj))
    return type(obj)


# [判断一个对象（包括）函数的类型]
import types


def judgeObjType(obj, type):
    if type(obj) == int:
        return 1
    elif type(obj) == str:
        return 2
    elif type(obj) == object:
        return 3
    elif type(obj) == types.FunctionType:
        return 4
    elif type(obj) == types.BuiltinFunctionType:
        print('这是一个内置函数')
        return 5
    elif type(obj) == types.LambdaType:
        print('这是一个lambda表达式')
        return 6
    elif type(obj) == types.GeneratorType:
        print('这是一个生成器generator')
        return 7
    else:
        return -1


print('===================================')
print('[获取对象所有属性]')
print('------')

print(dir(Person('Fang', 15)))

print('===================================')
print('[类似Java反射 -- 获取对象的属性和方法]')
print('------')

p = Person('Tom', 20)
print(hasattr(p, 'name'))
print(getattr(p, 'age'))
