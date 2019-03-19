class Person:
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return 'Person[name: {}]'.format(self._name)

class Employee(Person):
    def __init__(self, name, empId):
        Person.__init__(self, name)
        self.__empId = empId

    def __str__(self):
        return 'Employee[name: {}, empId: {}]'.format(self._name, self.__empId)


if __name__ == '__main__':
    p1 = Person('person1')
    print(p1)

    e1 = Employee('emp1', 1)
    print(e1)

    e2 = Employee('emp2', 2)
    print(e2)

print('inside employee module')
