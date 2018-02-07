class Stu:
    @property
    def id(self):
        return 12345

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value


ming = Stu()
ming.name = 'M'
print(ming.id, ming.name)
