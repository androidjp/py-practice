print('===================================')
print('[base64 加密解密]')
print('------')

import base64

ss = 'Hello 你好'
b = ss.encode(encoding='utf-8')
b64 = base64.b64encode(b)
print('encode', b64)

c = base64.b64decode(b64)
print('decode', c)
print('decode', str(c, 'utf-8'))
