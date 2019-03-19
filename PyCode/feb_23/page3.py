# numbers = list(range(1, 11))
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def square(n1):
    print('inside square: {}'.format(n1))
    return n1 * n1

def function1():
    for number in numbers:
        print('square: {}'.format(number * number))

# function1()

def function2():
    for number in numbers:
        print('square: {}'.format(square(number)))

# function2()

def function3():
    squares = []
    for number in numbers:
        squares.append(square(number))
    print(numbers)
    print(squares)

# function3()

def function4():
    squares = list(map(square, numbers))
    print(numbers)
    print(squares)

# function4()


def cube(number):
    print('inside cube: {}'.format(number))
    return number * number * number

def function5():
    cubes = []
    for number in numbers:
        value = cube(number)
        cubes.append(value)
    print(numbers)
    print(cubes)

# function5()

def function6():
    cubes = list(map(cube, numbers))
    print(numbers)
    print(cubes)

# function6()

def convertCelcius(t):
    return (t - 32) * 5 / 9

def function7():
    temperatures = [100, 98, 97, 96, 95, 100, 99]

    values = []
    for temperature in temperatures:
        values.append(convertCelcius(temperature))

    print(temperatures)
    print(values)

# function7()

def function8():
    temperatures = [100, 98, 97, 96, 95, 100, 99]
    values = list(map(convertCelcius, temperatures))
    print(temperatures)
    print(values)

# function8()








