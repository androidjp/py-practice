# coding=utf-8

import os


def main():
    print('Hello world, py!')


one = 1

print(one)
main()

if False:
    print('That is true')
else:
    print('that is false')

you = "Pan"
if you == "JP":
    print('You are JP')
elif you == "Pan":
    print("You are Pan")
else:
    print("Nothing")

# while
num = 1
while num <= 10:
    print(num)
    num += 1

loopCondition = True
while loopCondition:
    print('now is true')
    loopCondition = False
# for
for i in range(1, 5):
    print(i)

# list
my_int = [4, 2, 1, 3]
print(my_int[0])

listB = []
listB.append('AAA')
listB.append('NNN')
listB.append('BBB')
print(listB[0] + listB[2])

#########################

# data structure
dictionary_example = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}

dictionary_example2 = {
    "key3": "value3",
    "key4": "value3",
    "key5": "value3"
}

#########################
# loop for object
personList = [{
    "name": "Guo",
    "age": 20,
    "loop": "444"
}, {
    "name": "Guo",
    "age": 20,
    "loop": "444"
}
]
print('################')
for item in personList:
    for key in item:
        print("%s --> %s" % (key, personList[0][key]))

print('################')
personA = personList[0];
for attribute ,value in personA.items():
    print("PersonA's %s is %s" %(attribute, value))
