# importing entire module named person
import person

p1 = person.Person('person1', 45)
print(p1)


import car

c1 = car.Car('i20')
print(c1)

c2 = car.MyCar()
print(c2)

# from mobile module only Mobile class will get imported
# from mobile import Mobile
# from mobile import MyMobile
from mobile import Mobile, MyMobile

m1 = Mobile('Galaxy S10 plus')
print(m1)

m2 = MyMobile()
print(m2)