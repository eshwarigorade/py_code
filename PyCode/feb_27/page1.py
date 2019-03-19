class Person:
    # parameterless/default initializer
    # def __init__(self):

    # parameterized/custom initializer
    def __init__(self, name = '', email = '', age = 0):
        print('inside __init__')
        setattr(self, 'name', name)
        setattr(self, 'email', email)
        setattr(self, 'age', age)

    # def setInfo(self, name, email, age):
    #     setattr(self, 'name', name)
    #     setattr(self, 'email', email)
    #     setattr(self, 'age', age)

    def printInfo(self):
        print('name: {}'.format(getattr(self, 'name')))
        print('email: {}'.format(getattr(self, 'email')))
        print('age: {}'.format(getattr(self, 'age')))

    def canVote(self):
        if getattr(self, 'age') >= 18:
            print('{} is eligible for voting'.format(getattr(self, 'name')))
        else:
            print('{} is NOT eligible for voting'.format(getattr(self, 'name')))


def function2():
    p1 = Person('p1', 'p1@test.com', 45)
    p1.printInfo()

    p2 = Person()
    p2.printInfo()

function2()


def function1():
    count = int(input('how many person you want to create: '))
    persons = []
    for index in range(0, count):
        name = input('enter your name: ')
        email = input('enter your email: ')
        age = int(input('enter your age: '))

        p1 = Person(name, email, age)
        # p1.setInfo(name, email, age)

        persons.append(p1)

    # struct Person p;
    # struct Person p = (struct Person *) malloc(sizeof(struct Person);

    # print('you have entered: {}, {}, {}'.format(name, email, age))
    # print(p1.__dict__)
    print(persons)

    for person in persons:
        person.printInfo()
        person.canVote()

# function1()
