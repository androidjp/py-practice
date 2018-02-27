# encoding=utf-8
import re

print('===================================')
print('[re模块提供了 , r前缀让你不用考虑转义问题]')
print('------')

# compile 是为了节省重复编译正则表达式的时间。
pattern = re.compile(r'[\w]+')
match = pattern.match('hello world!')
if match:
    print('Match\n', match.group())

if re.compile(r'\d{4}-\d{2}-\d{2}').match('2017-01-21'):
    print('Success match 2017-01-21')

print('===================================')
print('[split(r\'正则\',目标string)]')
print('------')

print('case A:\n', re.split(r'\s+', 'a b   c'))

print('===================================')
print('[分组]')
print('------')

t = '19:05:20'
m = re.match(
    r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$',
    t)
print('识别时间并分组\n', m.groups())

print('===================================')
print('[贪婪匹配，正则默认是贪婪匹配，就是匹配尽可能多的字符串]')
print('------')

print('例子：\n', re.match(r'^(\d+)(0*)$', '102300').groups())
print('变成非贪婪匹配(后面的o*必须加括号)：\n', re.match(r'^(\d+?)(0*)$', '102300').groups())
