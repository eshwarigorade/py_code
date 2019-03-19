class Car:

    def setInfo(self, model, company, price):
        setattr(self, 'model', model)
        setattr(self, 'company', company)
        setattr(self, 'price', price)

    # setter method
    def setPrice(self, price):
        setattr(self, 'price', price)

    # getter method
    def getPrice(self):
        return getattr(self, 'price')

    # facilator method
    def printInfo(self):
        print('model: {}'.format(getattr(self, 'model')))
        print('company: {}'.format(getattr(self, 'company')))
        print('price: {}'.format(getattr(self, 'price')))

    # facilator method
    def canAfford(self):
        max = 5
        if getattr(self, 'price') <= max:
            print('YES :)')
        else:
            print('NO :(')

c1 = Car()
c1.setInfo('i20', 'hyundai', 7.5)
c1.printInfo()
c1.canAfford()

c2 = Car()
c2.setInfo('E2', 'mahindra', 1.50)
# c2.printInfo()
# setattr(c2, 'price', 'blahblah')
c2.setPrice(3.50)
# c2.printInfo()
print('c2 price = {}'.format(c2.getPrice()))
c2.canAfford()

