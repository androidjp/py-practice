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

print('===================================')
print('[datetime 转 string]')
print('------')

dt = datetime.now()
dtStr = dt.strftime('%Y-%m-%d %H:%M:%S %a %b')
print(dtStr)

print('===================================')
print('[datetime 加减]')
print('------')

from datetime import timedelta

dt = datetime.now()
print('Now:', dt)
dt += timedelta(hours=5, days=1)
print('+5h:', dt)

print('===================================')
print('[UTC -> Local]')
print('------')
# datetime 的tzinfo 属性默认为None , so, 默认无法确定dateTime的时区
from datetime import timezone

now = datetime.utcnow()
print('DEFAULT: ', now)
dt = now.replace(tzinfo=timezone.utc)
print('UTC: ', dt)
localTz = timezone(timedelta(hours=8))
local = dt.astimezone(localTz)
print('local: ', local)

print('===================================')
print('[local -> UTC]')
print('------')
now = datetime.now()
tz_utc_add8 = timezone(timedelta(hours=8))
localDt = now.replace(tzinfo=tz_utc_add8)
print('local:', localDt)
utc = localDt.astimezone(timezone.utc)
print('utc:', utc)
