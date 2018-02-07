print('===================================')
print('[命令行跑py, 带参数]')
print('------')

import sys


def init():
    args = sys.argv
    for item in args:
        print('Hello , ', item)
    pass


init()