class Person:
    def __init__(self):
        print('inside Person __init__')
        self.name = 'person1'
        self.address = 'Pune'
        self.phone = '+91234434'

# Student is-a Person
# Student is inherited from Person
# Student is derived from Person
class Student(Person):
    # initialize Student class object
    def __init__(self):
        # initialize Person class object within Student class object
        Person.__init__(self)
        self.roll = 1

# p1 = Person()
# print(p1.__dict__)
#
# s1 = Student()
# print(s1.__dict__)


class Vehicle:
    def __init__(self):
        # public
        self.model = ''
        self.company = ''

        # private
        self.__price = 0

class Bike(Vehicle):
    def __init__(self):
        Vehicle.__init__(self)


class Car(Vehicle):
    def __init__(self):
        Vehicle.__init__(self)
        self.doors = 2

    def print(self):
        print('model = {}'.format(self.model))
        print('company = {}'.format(self.company))
        print('price = {}'.format(self.__price))
        print('doors = {}'.format(self.doors))


v1 = Vehicle()
print(v1.__dict__)

c1 = Car()
print(c1.__dict__)
c1.print()





















