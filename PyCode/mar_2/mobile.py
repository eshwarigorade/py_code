class Mobile:
    def __init__(self, model):
        self.__model = model

    def __str__(self):
        return 'Mobile[model: {}]'.format(self.__model)

class MyMobile:
    pass


# m1 = Mobile('iPhone XS Max')
# print(m1)