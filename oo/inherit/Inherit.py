print('===================================')
print('[单继承]')
print('--------------')


class Animal:
    def cry(self):
        print(self.__class__.__name__, 'cry now!!!')


class Dog(Animal):
    pass


d = Dog()
d.cry()


print('===================================')
print('[多继承]')
print('--------------')

class RunnableMixln:
    def run(self):
        print(self.__class__.__name__, 'running !!!')

class Flyable:
    def fly(self):
        print(self.__class__.__name__, 'flying !!!')

class Bug(RunnableMixln, Flyable):
    pass

b = Bug()
b.fly()
b.run()
