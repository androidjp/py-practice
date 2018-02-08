print('===================================')
print('[os 获取系统信息如:路径等]')
print('------')

import os

print('os 类型:', os.name)  # nt: windows , posix: Linux ,MacOS
print('环境变量:', os.environ)
print(os.environ.get('PY_HOME'))

print('绝对路径:', os.path.abspath('.'))
print('绝对路径:', os.path.abspath('.'))

print('join:', os.path.join('/Users/michael', 'testdir'))

print('拆分路径： ', os.path.splitext('/path/to/file.txt'))
# mkdir(dir)
# rmdir(dir)
# rename(file)
# remove(file)

print('===================================')
print('[一行代码：过滤想要的文件]')
print('------')

list = [x for x in os.listdir('./../../') if os.path.isdir(os.path.join('./../../', x))]
print(list)
ll = [x for x in os.listdir('./') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
print(ll)
