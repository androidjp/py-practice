print('===================================')
print('[来一个除以0的异常方法，用try-catch-finally 的方式跑一跑]')
print('------')


def testMethod():
    res = 1 / 0
    print(res)
    pass


def main():
    try:
        testMethod()
    except Exception as Argument:
        print('This is Exception , ', Argument)
    else:
        print('success')
    finally:
        print('finally')


main()

print('===================================')
print('[自己抛异常]')
print('------')


def method2(man, tools):
    raise Exception('Have Bug', man, tools)
    pass


try:
    method2('刘东强', '剁手刀')
except Exception as e:
    for i, value in enumerate(e.args):
        print(i, value)
