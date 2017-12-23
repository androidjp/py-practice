# class of Python

class Vehicle:
    pass


car = Vehicle()
print(car)
print('##############')


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


class Person:
    def __init__(self, first_name, email):
        self.first_name = first_name
        self._email = email

    def update_email(self, new_email):
        self._email = new_email

    def email(self):
        return self._email

tk = Person('TK', 'tk@mail.com')
print(tk.email()) # => tk@mail.comtk._email = 'new_tk@mail.com'print(tk.email()) # => tk@mail.comtk.update_email('new_tk@mail.com')
tk._email = 'new_tk@mail.com'
print(tk.email())
tk.update_email('123@mail.com')
print(tk.email()) # => new_tk@mail.com