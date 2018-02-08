from io import StringIO, BytesIO

print('===================================')
print('[用StringIO 和 ByteIO 进行内存的读写]')
print('------')

f = StringIO()
f.write('12345')
f.write('Hello')
print(f.getvalue())

f = BytesIO('中国'.encode('utf-8'))
res = f.read()
print(res)
print(str(res, 'utf-8'))
