# class Person(object):
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def __del__(self):
        print('inside __del__')

    def __str__(self):
        return 'Person[name: {}, age: {}]'.format(self._name, self._age)

class Employee(Person):
    def __init__(self, name, age, employeeId):
        Person.__init__(self, name, age)
        self.__employeeId = employeeId

    def __str__(self):
        return 'Employee[name: {}, age: {}, empId: {}]'.format(self._name, self._age, self.__employeeId)

    def __lt__(self, other):
        if isinstance(other, Employee):
            return self._age < other._age
        else:
            print('the second parameter is not of type Employee')
            return False

class Manager(Employee):
    def __init__(self, name, age, employeeId, dept):
        Employee.__init__(self, name, age, employeeId)
        self.__dept = dept


# create an object
# instantiate Person
p1 = Person('person1', 45)
print(p1)
#
# # destroy
# del p1
#
e1 = Employee('emp1', 26, 1)
print(e1)

e2 = Employee('emp2', 28, 2)
print(e2)

m1 = Manager('m1', 45, 3, 'comp')

print(p1.__dir__())
print(Person.__bases__)
print(Employee.__bases__)
print(Manager.__bases__)

# e1.__lt__(e2)
print(e1 < e2)
print(e1 > e2)

# e1.__lt__(100)
print(e1 < 100)

print('is p1 an instance of Person: {}'.format(isinstance(p1, Person)))
print('is e1 an instance of Employee: {}'.format(isinstance(e1, Employee)))
print('is e1 an instance of Person: {}'.format(isinstance(e1, Person)))
print('is m1 an instance of Manager: {}'.format(isinstance(m1, Manager)))
print('is m1 an instance of Employee: {}'.format(isinstance(m1, Employee)))
print('is m1 an instance of Person: {}'.format(isinstance(m1, Person)))
print('is p1 an instance of Manager: {}'.format(isinstance(p1, Manager)))
print('is e1 an instance of Manager: {}'.format(isinstance(e1, Manager)))

p2 = p1

# p1 == p2
print('p1 and p2 are same: {}'.format(p1 is p2))
print('e1 and e2 are same: {}'.format(e1 is e2))

