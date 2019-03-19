class Person:
    def __init__(self, name, address, age):
        self._name = name
        self._address = address
        self._age = age

    def printInfo(self):
        print('----- from Person ------')
        print('name: {}'.format(self._name))
        print('address: {}'.format(self._address))
        print('age: {}'.format(self._age))

class Student(Person):
    def __init__(self, name, address, age, roll):
        Person.__init__(self, name, address, age)
        # private
        self.__roll = roll

    # Student is overriding the printInfo()
    def printInfo(self):
        print('----- from Student ------')
        print('roll: {}'.format(self.__roll))
        Person.printInfo(self)

class Monitor(Student):
    def __init__(self, name, address, age, roll, dummy):
        Student.__init__(self, name, address, age, roll)
        self.__dummy = dummy

    def printInfo(self):
        print('---- from Monitor -----')
        print('dummy: {}'.format(self.__dummy))
        Student.printInfo(self)

# p1 = Person('person1', 'Pune', 45)
# p1.printInfo()
#
# s1 = Student('student1', 'Karad', 23, 1)
# s1.printInfo()

m1 = Monitor('student2', 'Pune', 20, 2, 'dummy')
m1.printInfo()
