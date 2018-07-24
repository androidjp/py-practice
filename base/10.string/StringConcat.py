# 下面的写法：相当于 a,b 当成了一个元组
a, b = 'hello', 'world'
print('way 1:\n', a, b)

print('way 2:直接连接,是一种py的语法糖，这样拼接结果只会生成一个字符串对象\n', 'aaa''bbb')

print('way 3: 百分号\n', '%s %s' % ('aa', 'bb'))

print('way 4: format函数（Python 2.6中出现的，用于代替%操作符的字符串格式化方法）\n', '{} -- {}'.format('hello', 'world'))

print('way 5: join内置方法\n', '->'.join(['a', 'bb', 'ccc']))

print('way 6: f-string (Python 3.6 引入，全称 Formatted String Literals字面量格式化字符串)，是%和format的进化版\n', f'{a} + {b}')

print('way 7: 星号* ，对应的魔术方法是__mul__\n', 'hello ' * 3)

# 总结：
# 对性能较高要求+ python3.6以上：f-string
# 少量字符串：+
# 大量字符串：join 和f-string


