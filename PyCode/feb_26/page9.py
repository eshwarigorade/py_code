class Mobile:
    """
    please please please call setInfo before calling printInfo
    """

    # initializer method
    def __init__(self):
        print('inside __init__')
        setattr(self, 'model', '')
        setattr(self, 'company', '')
        setattr(self, 'price', 0)

    def setInfo(self, model, company, price):
        setattr(self, 'model', model)
        setattr(self, 'company', company)
        setattr(self, 'price', price)

    def setModel(self, model):
        setattr(self, 'model', model)

    def setCompany(self, company):
        setattr(self, 'company', company)

    def setPrice(self, price):
        setattr(self, 'price', price)

    def getModel(self):
        return getattr(self, 'model')

    def getCompany(self):
        return getattr(self, 'company')

    def getPrice(self):
        return getattr(self, 'price')

    def printInfo(self):
        print('model: {}'.format(getattr(self, 'model')))
        print('company: {}'.format(getattr(self, 'company')))
        print('price: {}'.format(getattr(self, 'price')))

m1 = Mobile()
# m1.__init__()
print(m1.__dir__())

# m1.setModel('S10+')
# m1.setCompany('Samsung')
# m1.setPrice(150000)
# m1.printInfo()


m2 = Mobile()
# m2.__init__()
# m2.setInfo('P20 Pro', 'Huawei', 85000)
# m2.printInfo()

# print(Mobile.__doc__)
m3 = Mobile()
m3.printInfo()