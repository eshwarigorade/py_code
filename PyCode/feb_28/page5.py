def function1():
    # creates an object of int class
    n1 = 5
    n2 = 21

    # result = n1.__add__(n2)
    # n1.__add__(n2)
    # result = n1 + n2
    # print('result: {}'.format(result))

    # true division
    # result1 = n1 / n2
    # print('result1 = {}'.format(result1))

    # floor division
    # result2 = n1 // n2
    # print('result2 = {}'.format(result2))

    # square = pow(n1, 2)
    square = n1 ** 2    # pow(n1, 2)
    print('square = {}'.format(square))

    cube = n1 ** 3      # pow(n1, 3)
    print('cube = {}'.format(cube))

# function1()

def function2():
    # creates an object of str class
    str1 = 'test1'
    str2 = 'test2'
    # str1.__add__(str2)
    print('result = {}'.format(str1 + str2))

# function2()


class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def printInfo(self):
        print('x: {}, y: {}'.format(self.__x, self.__y))

    def __mod__(self, other):
        print('inside __mod__')
        x = self.__x % other.__x
        y = self.__y % other.__y
        return Point(x, y)

    def __pow__(self, power, modulo=None):
        print('inside __pow__')
        x = self.__x ** power
        y = self.__y ** power
        return Point(x, y)

    def __truediv__(self, p2):
        print('inside __truediv__')
        x = self.__x / p2.__x
        y = self.__y / p2.__y
        return Point(x, y)

    def __floordiv__(self, p2):
        print('inside __floordiv__')
        x = self.__x // p2.__x
        y = self.__y // p2.__y
        return Point(x, y)

    def __mul__(self, other):
        print('inside __mul__')
        x = self.__x * p2.__x
        y = self.__y * p2.__y
        return Point(x, y)

    def __sub__(self, p2):
        print('inside __sub__')
        x = self.__x - p2.__x
        y = self.__y - p2.__y
        return Point(x, y)

    def __add__(self, p2):
        print('inside __add__')
        x = self.__x + p2.__x
        y = self.__y + p2.__y
        return Point(x, y)

p1 = Point(10, 20)
p1.printInfo()

p2 = Point(30, 40)
p2.printInfo()

# __add__(p1, p2)
# p3 = p1.__add__(p2)
# p3 = p1 + p2
# p3.printInfo()

# p4 = p1 - p2
# p4.printInfo()

# p4 = p1 * p2
# p4.printInfo()

# p4 = p1 / p2
# p4.printInfo()

# p4 = p1 // p2
# p4.printInfo()

# p1.__pow__(2)
# p4 = p1 ** 2
# p4.printInfo()

# p4 = p2 ** 4
# p4.printInfo()

# p1.__mod__(p2)
p4 = p1 % p2
p4.printInfo()

# print(p1.__dir__())
# p1.printMyInfo()
















