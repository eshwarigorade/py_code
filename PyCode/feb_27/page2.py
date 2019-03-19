class Car:
    def __init__(self, model = '', company = '', price = 0):
        # setattr(self, 'model', model)
        self.model = model

        # setattr(self, 'company', company)
        self.company = company

        # setattr(self, 'price', price)
        self.price = price

        # speed kmph
        # setattr(self, 'speed kmph', 100)
        # self.speed kmph = 100


    def printInfo(self):
        # print('model: {}'.format(getattr(self, 'model')))
        print('model: {}'.format(self.model))

        # print('company: {}'.format(getattr(self, 'company')))
        print('company: {}'.format(self.company))

        # print('price: {}'.format(getattr(self, 'price')))
        print('price: {}'.format(self.price))

c1 = Car('nano', 'tata', 1.5)
# print(c1.__dict__)
# c1.printInfo()
print('model: {}'.format(c1.model))
c1.company = 'garbage'
c1.price = 'blah blah blah'
print('model: {}'.format(c1.model))