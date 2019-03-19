class Car:
    def __init__(self, model):
        self.__model = model

    def __str__(self):
        return 'Car[model: {}]'.format(self.__model)

class MyCar:
    pass

if __name__ == '__main__':
    c1 = Car('i20')
    print(c1)