class Person:
    def __init__(self, name, email, age):
        self.__name = name      # _Person__name
        self.__email = email    # _Person__email
        self.__age = age        # _Person__age
        self.__password = 'test'

    def printInfo(self):
        print('name: {}'.format(self.__name))       # _Person__name
        print('email: {}'.format(self.__email))     # _Person__email
        print('age: {}'.format(self.__age))         # _Person__age


    def setPassword(self, value):
        self.__password = value

    def setAge(self, age):
        self.__age = age

    def getName(self):
        return self.__name

    def getEmail(self):
        return self.__email

    def getAge(self):
        return self.__age

p1 = Person('p1', 'p1@test.com', 45)
# setattr(p1, '__name', 'change')
# p1.__name = 'changed'
# p1.__email = 'test'
# p1.__age = 'damaged'
# p1._Person__name = 'test'
# print(p1.__dict__)
# p1.printInfo()
p1.setAge(50)
p1.setPassword('test1234')
print('name = {}'.format(p1.getName()))