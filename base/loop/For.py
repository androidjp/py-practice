print('===================================')
print('[普通for]')
print('------')

for i in range(1, 5):
    # print("Hi ," + i)
    print("Hi, ", i)

print('===================================')
print('[数组]')
print('------')

arr = ['A123', 'B', 'C', 100]
setA = {'A123', 'B', 'C', 100}
tupleA = ('A123', 'B', 'C', 100)
# for i in arr:
# for i in setA:
for i in tupleA:
    print('i = ', i)

print('===================================')
print('[数组 指定下标遍历]')
print('------')

arr = ['A123', 'B', 'C', 100]
for i in range(len(arr)):
    print(arr[i])

print('===================================')
print('[各种类型的内容遍历 , 结论：遍历的对象只能是数组或者字符串]')
print('------')

s1 = 'ABC'
for i in s1:
    print(i)
# int1 = 11111111
# for i in int1:
#     print(i)

print('===================================')
print('[break 和 continue]')
print('------')

for num in range(1, 20):
    # if num % 3 == 0:
    #     continue
    for i in range(2, num):
        if num % i == 0:
            j = num / i
            print('%d = %d * %d' % (num, i, j))
            break
    else:
        print(num)

        # public void contextLoads() {
        #     for (int i = 1; i < 20; i++) {
        #       boolean flag = true;
        #       for (int j = 2; j < i; j++) {
        # 				if(i%j == 0){
        # 				  int yuShu = i/j;
        #           System.out.printf("%d = %d * %d\n" , i, j, yuShu);
        #           flag = false;
        #           break;
        #         }
        #       }
        #       if(flag){
        #         System.out.println(i);
        #       }
        #     }
        #   }
