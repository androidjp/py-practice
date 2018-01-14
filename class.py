# class of Python
from typing import Any


class Vehicle:
    pass


car = Vehicle()
print(car)
print('===========================')
print('第一个类的定义')
print('===========================')


class Vehicle:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def age(self):
        return self.age

    def name(self):
        return self.name

    def setAge(self, age):
        self.age = age

    pass


v1 = Vehicle(18, '小明')
print(v1.age)
print(v1.name)
Vehicle.setAge(v1, 9)
print(v1.age)

print('===========================')
print('关于getter 和 setter的定义和使用')
print('===========================')

class Person:
    def __init__(self, first_name, email):
        self.first_name = first_name
        self._email = email

    def update_email(self, new_email):
        self._email = new_email

    def email(self):
        return self._email

tk = Person('TK', 'tk@mail.com')
print(tk.email())
tk._email = 'new_tk@mail.com'
print(tk.email())
tk.update_email('123@mail.com')
print(tk.email()) # => new_tk@mail.com

print("====================================")
print("真正的private属性:")
print("====================================")

class Obj2:
    value = "Ming"
    def __init__(self):
        self.__id = None

obj2 = Obj2()
print(obj2.value)
bol = True if obj2.value is None else False
print(bol)

print("====================================")
print("类内部实现toString")
print("====================================")

class student:
    name:None
    age:None
    sex:None

    def __getattribute__(self, name: str) -> Any:
        return super().__getattribute__(name)

    def toString(self):
        for key, value in vars(self).items():
            print("%s --> %s" %(key, value))
    pass

stuA = student()
stuA.name = "A"
stuA.age = 18
stuA.sex = True
stuA.toString()



