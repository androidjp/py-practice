print('===================================')
print('[节省内存空间的 生成器 ，某些情况代替了数组]')
print('--------------')

g = (x * x for x in range(1, 100000))
print(next(g))
print(next(g))
print(next(g))

print('===================================')
print('[将普通方法变成一个 generator]')
print('--------------')

# 斐波那契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


f = fib(10)
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))

def steps():
    yield 'stepA'
    yield 'stepB'
    while True:
        yield 'StepN'

s = steps()
print(next(s))
print(next(s))
print(next(s))
print(next(s))