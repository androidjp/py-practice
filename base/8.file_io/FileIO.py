print('===================================')
print('[只读文件：`open(`path`,`r`)`]')
print('[读byte出来：`open(`path`,`rb`)`]')
print('[读gbk编码的文件：`open(`path`,`r`,encoding=`GBK`, errors=`ignore`)`]')
print('------')

with open('./../README.md', 'r', encoding='UTF-8') as f:
    print(f.read())

print('===================================')
print('[写文件（覆盖）：`open(`path`,`w`)`]]')
print('[写文件（追加）：`open(`path`,`a`)`]]')
print('------')

with open('./../README.md', 'a') as f:
    f.write('\n* Good!')
