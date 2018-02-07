print('===================================')
print('[python 写函数的特别之处：]')
print('------')

print('===================================')
print('[指定传入参数的默认值]')
print('------')


def mthd(config='DEFAULT'):
    print(config)


mthd()
mthd('YEAH')

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

print('===================================')
print('[函数作为返回值]')
print('--------------')


def count(args):
    def sum():
        result = 0
        for i in args:
            result += i
        return result

    return sum


f = count([1, 2, 3, 4])
print(f())

print('===================================')
print('[闭包 与 经典的循环问题]')
print('------')


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())

print('改进后：')


def count():
    fs = []

    def f(i):
        def g():
            return i * i

        return g

    for n in range(1, 4):
        fs.append(f(n))

    return fs


f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())

print('===================================')
print('[装饰器 -- Python 上的 AspectJ (接收函数,返回装饰后的新函数)]')
print('------')


def say(s):
    print('Say:', s)


def winter_env(func, weather='WINTER'):
    def wrapper(*args, **kw):
        print('In %s, call %s():' % (weather, func.__name__))
        return func(*args, **kw)

    return wrapper


winter_env(say)('Hello,I\'m so happy!')

print('===================================')
print('[换一种写法：Python的@方式]')
print('------')


# 换一种类Java的写法
@winter_env
def ride_bike(who):
    print(who, ' riding bike.')


ride_bike('Jasper')

print('===================================')
print('[带上参数的注解方式的装饰器]')
print('------')

# 如果我想注解上传入参数怎么玩？
# from functools import wraps
import functools


def db_config(dbUrl, userName, password):
    def dectorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            dictDB = {'dbUrl': dbUrl, 'userName': userName, 'password': password}
            print('--------------')
            for k, v in dictDB.items():
                print(k, ":", v)
            print('--------------')
            return func(*args, **kw)

        return wrapper

    return dectorator


@db_config(dbUrl='http://localhost:3006/test', userName='admin', password='123')
def init():
    print('初始化完毕')


init()

rf = db_config(dbUrl='http://localhost:3006/test', userName='admin', password='123')(init)
rf()

print('===================================')
print('[关于@functools.wraps , 将作用域正确绑定]')
print('------')
print(rf.__name__)

print('===================================')
print('[偏函数 -> 更快捷的方法重写]')
print('------')

int2 = functools.partial(int, base=2)
int16 = functools.partial(int, base=16)
print(int16('0x0F'))
# kw = { 'base': 2 }
# int('10010', **kw)
