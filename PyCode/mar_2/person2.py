class Person:
    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return 'Person2 [name: {}]'.format(self.__name)

