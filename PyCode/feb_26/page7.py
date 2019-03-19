class Person:

    # method
    # first parameter MUST be a self
    def setInfo(self, name, email, phone, age):
        setattr(self, 'name', name)
        setattr(self, 'email', email)
        setattr(self, 'phone', phone)
        setattr(self, 'age', age)

    def print(self):
        print('name: {}'.format(getattr(self, 'name')))
        print('email: {}'.format(getattr(self, 'email')))
        print('phone: {}'.format(getattr(self, 'phone')))
        print('age: {}'.format(getattr(self, 'age')))

    def canVote(self):
        if getattr(self, 'age') >= 18:
            print('YES')
        else:
            print('NO')

    def dummy(self):
        print('inside dummy')

p1 = Person()
p1.setInfo('p1', 'p1@test.com', '+91334', 45)
# setInfo(p1, 'p1', 'p1@test.com', '+91334', 45)
p1.print()
p1.canVote()
p1.dummy()
# dummy(p1)

# print(p1)
# print(p1.__dict__)
# print(p1.__dir__())

p2 = Person()
p2.setInfo('p2', 'p2@test.com', '+913345', 15)
p2.print()
p2.canVote()
p2.dummy()