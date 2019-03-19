def add(p1, p2):
    print('addition = {}'.format(p1 + p2))

def multiply(p1, p2):
    print('multiplication = {}'.format(p1 * p2))

def divide(p1, p2):
    print('division = {}'.format(p1 / p2))

def subtract(p1, p2):
    print('subtraction = {}'.format(p1 - p2))


# myAdd = add
# myAdd1 = myAdd
# myAdd2 = myAdd1
# myMultiply = multiply
#
# myAdd(10, 40)
# myMultiply(30, 40)

# # 10, 20
# add(10, 20)
# multiply(10, 20)
#
# # 40, 50
# add(40, 50)
# multiply(40, 50)
#
# # 60, 70
# add(60, 70)
# multiply(60, 70)
#
# # 80, 90
# add(80, 90)
# multiply(80, 90)


def execute(f1):
    # function alias
    # f1 = add
    print('----------')
    f1(10, 20)
    f1(40, 50)
    f1(60, 70)
    f1(80, 90)
    print('----------')

# execute(add)
# execute(multiply)
# execute(divide)
# execute(subtract)

def execute2(*functions):
    print(functions)
    for func in functions:
        func(10, 20)
        func(40, 50)
        func(60, 70)
        func(80, 90)

execute2(add, multiply, divide, subtract)