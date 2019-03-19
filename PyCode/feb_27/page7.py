class Person:
    def __init__(self, name, address, age):
        self.__name = name
        self.__address = address
        self.__age = age

    # def setCar(self, model, company, price):
    #     self.__model = model
    #     self.__company = company
    #     self.__price = price

    def setCar(self, car):
        self.__car = car

    def printPerson(self):
        print('{}, {}, {}'.format(self.__name, self.__address, self.__age))
        print('owns')
        self.__car.printCar()
        # print('model: {}'.format(self.__car.__model))


class Car:
    def __init__(self, model, company, price):
        self.__model = model
        self.__company = company
        self.__price = price

    def printCar(self):
        print('{}, {}, {}'.format(self.__model, self.__company, self.__price))

c1 = Car('nano', 'tata', 1.5)
c1.printCar()

p1 = Person('person1', 'Pune', 45)
p1.setCar(c1)

# p1.setCar('nano', 'tata', 1.5)
p1.printPerson()

c2 = Car('E2', 'mahindra', 1.5)
p1.setCar(c2)
p1.printPerson()


