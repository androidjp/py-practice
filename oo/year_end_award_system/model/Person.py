class Person:
    __salary: None

    def __init__(self, name, age):
        self.name = name
        self.age = age
        pass

    def getSalary(self):
        return self.__salary * 0.8

    def setSalary(self, salary):
        self.__salary = salary
