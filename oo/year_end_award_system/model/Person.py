class Person:
    # 定义允许被绑定的属性名称
    __slots__ = ('name', 'age', '__salary')

    def __init__(self, name, age):
        self.name = name
        self.age = age
        pass

    def getSalary(self):
        return self.__salary * 0.8

    def setSalary(self, salary):
        self.__salary = salary

    def __str__(self):
        return 'name:' + self.name + ',age:' + str(self.age)

    __repr__ = __str__

    # def toString(self):
    #     res = ''
    #     for key, value in vars(self).items():
    #         # print("%s --> %s" % (key, value))
    #         res += ' ('
    #         res += key
    #         res += ' - '
    #         res += str(value)
    #         res += ') '
    #     return res
