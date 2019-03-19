numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def function1():
    evenNumbers = []
    for number in numbers:
        if number % 2 == 0:
            evenNumbers.append(number)
    print(numbers)
    print(evenNumbers)

# function1()

def isEven(number):
    return number % 2 == 0
    # if number % 2 == 0:
    #     return True
    # else:
    #     return False


def function2():
    evenNumbers = []
    for number in numbers:
        if isEven(number):
            evenNumbers.append(number)

    print(numbers)
    print(evenNumbers)

# function2()

def function3():
    evenNumbers1 = list(map(isEven, numbers))
    evenNumbers2 = list(filter(isEven, numbers))
    print(numbers)
    print(evenNumbers1)
    print(evenNumbers2)

# function3()



def function4():
    squares = list(map(lambda x: x * x, numbers))
    print(numbers)
    print(squares)

    evenNumbers = list(filter(lambda x: x % 2 == 0, numbers))
    print(evenNumbers)

    oddNumbers = list(filter(lambda x: x % 2 != 0, numbers))
    print(oddNumbers)

# function4()

def function5():
    # squareEvenNumbers = [4, 16, 36, 64, 100]

    squareEvenNumbers = []
    for number in numbers:
        # filter
        if number % 2 == 0:
            # map
            squareEvenNumbers.append(number * number)
    print(squareEvenNumbers)

# function5()

def function6():
    evenNumbers = list(filter(lambda x: x % 2 == 0, numbers))
    squareEvenNumbers = list(map(lambda x: x * x, evenNumbers))
    print(squareEvenNumbers)

# function6()

def function7():
    oddNumbers = list(filter(lambda x: x % 2 != 0, numbers))
    cubeOddNumbers = list(map(lambda x: x * x * x, oddNumbers))
    print(cubeOddNumbers)

# function7()


def function8():
    max = 10
    cars = [
        ('i20', 'hyundai', 7.5),  # Yes
        ('innova', 'toyota', 25.5),  # No
        ('nano', 'tata', 2.5)  # Yes
    ]

    affordableCars = list(filter(lambda car: car[2] <= max, cars))
    print(cars)
    print(affordableCars)

# function8()

def function9():
    max = 50000
    mobiles = [
        {'model': 'Note 5 Pro', 'company': 'Xiaomi', 'price': 17000},
        {'model': 'iPhone XS Max', 'company': 'Apple', 'price': 145000},
        {'model': 'Galaxy S10+', 'company': 'Sumsung', 'price': 100000},
        {'model': 'One Plus 6', 'company': 'One Plus', 'price': 40000},
        {'model': 'Z10', 'company': 'BlackBerry', 'price': 40000}
    ]

    affordablePhones = list(filter(lambda phone: phone['price'] <= max, mobiles))
    print(affordablePhones)

function9()






