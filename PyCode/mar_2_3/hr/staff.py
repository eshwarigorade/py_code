class Staff:
    def __init__(self, name, email, type):
        self.__name = name
        self.__email = email
        self.__type = type


    def __str__(self):
        return 'Staff[name: {}, email: {}, type: {}]'.format(self.__name, self.__email, self.__type)

if __name__ == '__main__':
    pass