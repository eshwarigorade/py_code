class Person:
    """
    represents a person
    """
    pass

def setInfo(person, name, email, phone, age):
    setattr(person, 'name', name)
    setattr(person, 'email', email)
    setattr(person, 'phone', phone)
    setattr(person, 'age', age)

def printPerson(person):
    print('name: {}'.format(getattr(person, 'name')))
    print('email: {}'.format(getattr(person, 'email')))
    print('phone: {}'.format(getattr(person, 'phone')))
    print('age: {}'.format(getattr(person, 'age')))

def canVote(person):
    age = getattr(person, 'age')
    if age >= 18:
        print('YES')
    else:
        print('NO')


p1 = Person()
setInfo(p1, 'person1', 'person1@test.com', '+912342424', 45)
printPerson(p1)
canVote(p1)

p2 = Person()
setInfo(p2, 'person2', 'person2@test.com', '+912342425', 15)
printPerson(p2)
canVote(p2)
