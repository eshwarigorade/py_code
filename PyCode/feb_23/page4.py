numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def square(n):
    return n * n

def function1():
    squares = list(map(square, numbers))
    print(numbers)
    print(squares)

# function1()

def funcition2():
    squares = list(map(lambda x: x * x, numbers))
    print(numbers)
    print(squares)

# funcition2()

def add(p1, p2):
    return p1 + p2

def execute(f1):
    # function alias
    # f1 = add
    # f1 = lambda x, y: x + y
    print('----------')
    print('result = {}'.format(f1(10, 20)))
    print('result = {}'.format(f1(40, 50)))
    print('result = {}'.format(f1(60, 70)))
    print('result = {}'.format(f1(80, 90)))
    print('----------')

# execute(add)

# execute(lambda x, y: x + y)
# execute(lambda x, y: x * y)
# execute(lambda n1, n2: n1 - n2)
# execute(lambda p1, p2: p1 / p2)
# execute(lambda x, y: (x + y, x  - y))

def function3():
    temperatures = [100, 98, 97, 96, 95, 100, 99]
    values = list(map(lambda t: (t-32) * 5 / 9, temperatures))
    print(temperatures)
    print(values)

function3()
