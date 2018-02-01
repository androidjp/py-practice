class Student:
    _salary: None

    def __init__(self, name, age):
        self.name = name
        self.age = age
        pass

    def getSalary(self):
        return self._salary / 100

    def setSalary(self, salary):
        self._salary = salary * 0.8


