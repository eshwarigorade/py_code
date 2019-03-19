class Person:
    def __init__(self):
        self.name = 'person1'

class Employee(Person):
    def __init__(self):
        Person.__init__(self)
        self.employeeId = 1

class Manager(Employee):
    def __init__(self):
        Employee.__init__(self)
        self.department = 'comp'

p1 = Person()
e1 = Employee()
m1 = Manager()

print(p1.__dict__)
print(e1.__dict__)
print(m1.__dict__)

