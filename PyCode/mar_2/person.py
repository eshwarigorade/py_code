class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __str__(self):
        return 'Person[name: {}, age: {}]'.format(self.__name, self.__age)

if __name__ == '__main__':
    p1 = Person('person1', 45)
    print(p1)
    print('person: __name__ -> {}'.format(__name__))
