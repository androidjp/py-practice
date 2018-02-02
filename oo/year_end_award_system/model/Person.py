class Person:
    __salary: 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        pass

    def getSalary(self):
        return self.__salary * 0.8

    def setSalary(self, salary):
        self.__salary = salary

    def toString(self):
        res = ''
        for key, value in vars(self).items():
            # print("%s --> %s" % (key, value))
            res += ' ('
            res += key
            res += ' - '
            res += str(value)
            res += ') '
        print(res)
    pass
