# python 字符串  是 Unicode 编码
# coding=UTF-8
print('===================================')
print('[A的Unicode: ]', ord('A'))
print('------')

print('===================================')
print('[Uncode 转 字符: ]', chr(25991))
print('------')

print('===================================')
print('[字符的整数编码 直接会读成 字符本身：]', '\u4e2d\u6587')
print('------')

print('===================================')
print('[Python字符串 转 byte 后进行IO操作, 相当于：多字节格式 变成 单字节格式]', b'ABC')
print('------')

print('===================================')
print('[4.encode 指定编码 进行转换, 从字符变成byte]', '1A3'.encode('utf-8'))
print('------')

print('===================================')
print('[decode 指定解码 进行转换, 从byte变成字符]', b'1A3'.decode('utf-8'))
print('------')
#在bytes中，无法显示为ASCII字符的字节，用\x##显示
print('===================================')
print('[解码时，忽略错误字节，用ignore]', b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))
print('------')

print('===================================')
print('[计算长度]')
print('------')

print(len('ABC'))
print(len(b'ABC'))
print(len('ABC'.encode('utf-8')))
print(len('中文'))
print(len('中文'.encode('utf-8')))
