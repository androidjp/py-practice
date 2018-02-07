from datetime import datetime

print('===================================')
print('[获取当前的时间]')
print('--------------')

print(datetime.now())

dt = datetime(2018, 4, 2, 12, 20, 59, 999999)
print(dt)

print('===================================')
print('[datetime 转 timestamp]')
print('--------------')

dt = datetime(2018, 4, 2, 12, 20, 59, 999999)
print(dt.timestamp())

print('===================================')
print('[timestamp 转  datetime]')
print('--------------')

ts = datetime.now().timestamp()
print(datetime.fromtimestamp(ts))

print('UTC : ', datetime.utcfromtimestamp(ts))

print('===================================')
print('[string 转 datetime]')
print('--------------')

timeStr = '2015-3-15 18:19:59'
cday = datetime.strptime(timeStr, '%Y-%m-%d %H:%M:%S')
print(cday)
