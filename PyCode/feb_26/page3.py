
def printPersonT(p):
    print('name: {}'.format(p[0]))
    print('email: {}'.format(p[1]))
    print('phone: {}'.format(p[2]))
    print('age: {}'.format(p[3]))

# name, email, phone, age
# person = ['person1', 'person1@test.com',  '+91334234', 45]
# person1 = ('person1', 'person1@test.com', '+91334234', 45)
# printPersonT(person1)
#
# person2 = ('person2', '+91334235', 15, 'person2@test.com')
# printPersonT(person2)

def printPersonD(p):
    print('name: {}'.format(p['name']))
    print('email: {}'.format(p['email']))
    print('phone: {}'.format(p['phone']))
    print('age: {}'.format(p['age']))

def canVote(p):
    if p['age'] >= 18:
        print('YES')
    else:
        print('NO')

# printPersonD(10)

p1 = {'name': 'person1', 'email': 'person1@test.com', 'phone': '+912344334', 'age': 45}
printPersonD(p1)
canVote(p1)

p2 = {'name': 'person2', 'phone': '+912344335', 'age': 15, 'email': 'person2@test.com'}
printPersonD(p2)
canVote(p2)

# name: steve, age: 64, pincode: 41101, phone: 3453555, place: NY