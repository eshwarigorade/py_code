class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __del__(self):
        print('inside __del__')

    def __str__(self):
        return 'name: {}, age: {}'.format(self.__name, self.__age)

    def __lt__(self, other):
        print('inside __lt__')
        return self.__age < other.__age

    def __gt__(self, other):
        print('inside __gt__')
        return self.__age > other.__age

    def __le__(self, other):
        print('inside __le__')
        return self.__age <= other.__age

    def __ge__(self, other):
        print('inside __ge__')
        return self.__age >= other.__age

    def __eq__(self, other):
        print('inside __eq__')
        return (self.__age == other.__age) and (self.__name == other.__name)

    def __ne__(self, other):
        print('inside __ne__')
        return (self.__age != other.__age) and (self.__name != other.__name)

    # def printInfo(self):
    #     print('name: {}'.format(self.__name))
    #     print('age: {}'.format(self.__age))

p1 = Person('person1', 45)
print(p1)   # print(p1.__str__())

p2 = Person('person2', 15)
print(p2)   # print(p1.__str__())

# print(p1.__dir__())
# p1.__lt__(p2)
print('p1 < p2: {}'.format(p1 < p2))

# p1.__gt__(p2)
print('p1 > p2: {}'.format(p1 > p2))

# p1.__le__(p2)
print('p1 <= p2: {}'.format(p1 <= p2))

# p1.__ge__(p2)
print('p1 >= p2: {}'.format(p1 >= p2))

# p1.__eq__(p2)
print('p1 == p2: {}'.format(p1 == p2))

# p1.__ne__(p2)
print('p1 != p2: {}'.format(p1 != p2))


n1 = 10
n2 = 20

# n1 < n2 => n1.__lt__(n2)
# print('n1 < n2: {}'.format(n1 < n2))


# str1 = p1.__str__()
# print('type of p1: {}, type of str1: {}'.format(type(p1), type(str1)))

# num.__str__
# num = 100
# # print('num = {}'.format(num.__str__()))
#
# str1 = num.__str__()
# print('type of num: {}, type of str1: {}'.format(type(num), type(str1)))