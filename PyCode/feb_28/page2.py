class Address:
    def __init__(self, city, state, country, zipcode):
        print('inside Address __init__')
        self.__city = city
        self.__state = state
        self.__country = country
        self.__zipcode = zipcode

    def printAddress(self):
        print('city: {}'.format(self.__city))
        print('state: {}'.format(self.__state))
        print('country: {}'.format(self.__country))
        print('zipcode: {}'.format(self.__zipcode))

    def __del__(self):
        print('inside Address __del__')


class Person:
    # initialize the object
    # automatically gets called for every object when the object gets created
    def __init__(self, name, email, age, city, state, country, zipcode):
        print('inside Person __init__')
        self.__name = name
        self.__email = email
        self.__age = age
        self.__address = Address(city, state, country, zipcode)

    # de-initialize the object
    # automatically gets called for every object at the time of deleting the object
    def __del__(self):
        print('inside Person __del__')
        del self.__address

    def printInfo(self):
        print('name: {}'.format(self.__name))
        print('email: {}'.format(self.__email))
        print('age: {}'.format(self.__age))
        self.__address.printAddress()



p1 = Person('person1', 'p1@test.com', 45, 'Pune', 'MH', 'India', 411041)
del p1
#
# p2 = Person('person1', 'p1@test.com', 45, 'Pune', 'MH', 'India', 411041)
# del p2
#
# p3 = Person('person1', 'p1@test.com', 45, 'Pune', 'MH', 'India', 411041)
# del p3


class Car:
    def __init__(self):
        print('inside Car __init__')

    def __del__(self):
        print('inside Car __del__')

# struct Car *c1 = (struct Car *) malloc(sizeof(struct Car));
# c1 = Car()
# print(c1.__dir__())

# free(c1);
# del c1



# class Company:
#     def __init__(self, name, employeeCount, city, state, country, zipcode):
#         self.__name = name
#         self.__employeeCount = employeeCount
#         self.__address = Address(city, state, country, zipcode)
#
#     def printInfo(self):
#         print('name: {}'.format(self.__name))
#         print('employee count: {}'.format(self.__employeeCount))
#         self.__address.printAddress()
#
# c1 = Company('Apple', 150000, 'Pune', 'MH', 'India', 411041)
# c1.printInfo()