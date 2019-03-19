
def function1():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    squares = list(map(lambda x: x * x, numbers))
    cubes = list(map(lambda x: x * x * x, numbers))
    print(numbers)
    print(squares)
    print(cubes)

# function1()


def function2():
    max = 10
    cars = [
        ('i20', 'hyundai', 7.5),        # Yes
        ('innova', 'toyota', 25.5),     # No
        ('nano', 'tata', 2.5)           # Yes
    ]
    # for car in cars:
    #     if car[2] >= max:
    #         print('No')
    #     else:
    #         print('Yes')
    # answers = list(map(lambda car: car[2] <= max, cars))
    # print(answers)

    prices = list(map(lambda car: 'price: {}'.format(car[2]), cars))
    print(prices)


# function2()
