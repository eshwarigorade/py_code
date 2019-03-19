class Person:
    def __init__(self, name, address, age):
        # protected
        self._name = name
        self._address = address
        self._age = age

    def printPersonInfo(self):
        print('name: {}'.format(self._name))
        print('address: {}'.format(self._address))
        print('age: {}'.format(self._age))

class Student(Person):
    def __init__(self, name, address, age, roll):
        Person.__init__(self, name, address, age)
        # private
        self.__roll = roll

    def printStudentInfo(self):
        print('name: {}'.format(self._name))
        print('address: {}'.format(self._address))
        print('age: {}'.format(self._age))
        print('roll: {}'.format(self.__roll))


# p1 = Person('person1', 'Pune', 45)
# p1.printPersonInfo()

s1 = Student('student1', 'Karad', 23, 1)
s1.printPersonInfo()
s1.printStudentInfo()