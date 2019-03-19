class Person:
    """
    represents a person
    """
    pass

# object of Person class
p1 = Person()

# add a person's information
setattr(p1, 'name', 'person1')
setattr(p1, 'email', 'person1@test.com')
setattr(p1, 'phone', '+912323424')
setattr(p1, 'age', 45)

# print(p1)
# print(p1.__doc__)
# print(p1.__dict__)
# print(p1.__class__)

# retrieve the person info
print('name: {}'.format(getattr(p1, 'name')))
print('email: {}'.format(getattr(p1, 'email')))
print('phone: {}'.format(getattr(p1, 'phone')))
print('age: {}'.format(getattr(p1, 'age')))

p2 = Person()

setattr(p2, 'name', 'person2')
setattr(p2, 'email', 'person2@test.com')
setattr(p2, 'phone', '+912323425')
setattr(p2, 'age', 15)

print('name: {}'.format(getattr(p2, 'name')))
print('email: {}'.format(getattr(p2, 'email')))
print('phone: {}'.format(getattr(p2, 'phone')))
print('age: {}'.format(getattr(p2, 'age')))



