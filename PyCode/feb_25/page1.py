numbers = list(range(1, 11))

def function1():
    """
    using a for..in loop
    """
    print('inside function1')
    squares = []
    for number in numbers:
        squares.append(number * number)
    print(squares)

# function1()

def function2():
    """
    using a map function
    """
    print('inside function2')
    squares = list(map(lambda x: x * x, numbers))
    print(squares)

# function2()

def function3():
    """
    using list comprehension
    """
    print('inside function3')
    squares = [number * number for number in numbers]
    print(squares)

# function3()

def function4():
    # cubes1 = list(map(lambda x: x * x * x, numbers))
    # print(cubes1)

    # cubes1 = [number * number * number for number in numbers]
    # print(cubes1)

    numbers2 = [(n, n * n, n * n * n) for n in numbers]
    print(numbers2)

    numbers3 = list(map(lambda n: (n, n * n, n * n * n), numbers))
    print(numbers3)

# function4()

def function5():
    distances = [1000, 30000, 50000, 60000]

    distances1 = list(map(lambda x: x / 1000, distances))
    print(distances1)

    distances2 = [distance / 1000 for distance in distances]
    print(distances2)

    distances3 = [(distance, distance / 1000) for distance in distances]
    print(distances3)


# function5()

def function6():
    cars = [
        {'model': 'i20', 'company': 'hyudai', 'price': 7.5},
        {'model': 'i10', 'company': 'hyudai', 'price': 5.5},
        {'model': 'fabia', 'company': 'skoda', 'price': 6.5},
        {'model': 'nano', 'company': 'tata', 'price': 1.5}
    ]

    result1 = list(map(lambda car: (car['model'], car['price']), cars))
    print(result1)

    result2 = [(car['model'], car['price']) for car in cars]
    print(result2)

# function6()


def function7():
    result1 = [(n, n * n, n * n * n) for n in numbers]
    print(result1)

    result2 = [(n, n + 1) for n in numbers]
    print(result2)

function7()










