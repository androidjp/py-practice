from contextlib import contextmanager, closing

print('===================================')
print('[不只是IO, 对象方法调用也能用with]')
print('------')


# ATE coding 例子
class ATE:
    # def __enter__(self):
    #     print('开机,开IDE')
    #     return self

    def coding(self):
        print(self.__class__.__name__, 'coding ....')

        # def __exit__(self, exc_type, exc_val, exc_tb):
        #     if exc_type:
        #         print('Error')
        #     else:
        #         print('关IDE,关机')


j = ATE()
# with ATE() as j:
j.coding()

print('===================================')
print('[用装饰器@contextmanager 代替 __enter__ 和 __exit__]')
print('------')


@contextmanager
def j_coding():
    print('开机')
    j = ATE()
    yield j
    print('关机')


with j_coding() as j:
    j.coding()

print('===================================')
print('[@closing 将普通对象 变成 可用 with 的对象]')
print('------')

# from urllib.request import urlopen
#
# with closing(urlopen('https://www.python.org')) as page:
#     for line in page:
#         print(line)