# Person has-a address
# Company has-a address
# Address: city, state, country, zipcode

class Person:
    def __init__(self, name, email, age, city, state, country, zipcode):
        self.__name = name
        self.__email = email
        self.__age = age
        self.__city = city
        self.__state = state
        self.__country = country
        self.__zipcode = zipcode

    def printInfo(self):
        print('name: {}'.format(self.__name))
        print('email: {}'.format(self.__email))
        print('age: {}'.format(self.__age))
        print('city: {}'.format(self.__city))
        print('state: {}'.format(self.__state))
        print('country: {}'.format(self.__country))
        print('zipcode: {}'.format(self.__zipcode))

# p1 = Person('person1', 'p1@test.com', 45, 'Pune', 'MH', 'India', 411041)
# p1.printInfo()

class Company:
    def __init__(self, name, employeeCount, city, state, country, zipcode):
        self.__name = name
        self.__employeeCount = employeeCount
        self.__city = city
        self.__state = state
        self.__country = country
        self.__zipcode = zipcode

    def printInfo(self):
        print('name: {}'.format(self.__name))
        print('employee count: {}'.format(self.__employeeCount))
        print('city: {}'.format(self.__city))
        print('state: {}'.format(self.__state))
        print('country: {}'.format(self.__country))
        print('zipcode: {}'.format(self.__zipcode))

# c1 = Company('Apple', 150000, 'Pune', 'MH', 'India', 411041)
# c1.printInfo()