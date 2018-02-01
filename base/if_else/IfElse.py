print('===================================')
print('[例子A]')
print('------')

if False:
    print('That is true')
else:
    print('that is false')

print('===================================')
print('[例子B]')
print('------')

you = "A"
if you == "B":
    print('You are B')
elif you == "A":
    print("You are A")
else:
    print("Nothing")

print('===================================')
print('[三元表达式这样写：]')
print('------')

bol = True if 2 + 3 != 5 else False
print(bol)