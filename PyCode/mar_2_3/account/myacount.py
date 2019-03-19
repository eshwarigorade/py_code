class MyAccount:
    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return 'MyAccount[name: {}]'.format(self.__name)

