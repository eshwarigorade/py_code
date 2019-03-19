numbers = list(range(1, 11))

def function1():
    print('function1')
    evenNumbers = []
    for number in numbers:
        if number % 2 == 0:
            evenNumbers.append(number)

    print(evenNumbers)

# function1()

def function2():
    print('function2')
    evenNumbers = list(filter(lambda x: x % 2 == 0, numbers))
    print(evenNumbers)

# function2()

def function3():
    print('function3')
    evenNumbers = [number for number in numbers if number % 2 == 0]
    print(evenNumbers)

    oddNumbers = [number for number in numbers if number % 2 != 0]
    print(oddNumbers)

# function3()

def function4():
    max = 5
    cars = [
        {'model': 'i20', 'company': 'hyudai', 'price': 7.5},
        {'model': 'i10', 'company': 'hyudai', 'price': 5.0},
        {'model': 'fabia', 'company': 'skoda', 'price': 6.5},
        {'model': 'nano', 'company': 'tata', 'price': 1.5}
    ]

    result1 = list(filter(lambda car: car['price'] <= max, cars))
    result2 = list(map(lambda car: car['model'], result1))
    result3 = list(map(lambda car: car['company'], result1))
    print(result2)
    print(result3)

# function4()

def function5():
    max = 5
    cars = [
        {'model': 'i20', 'company': 'hyudai', 'price': 7.5},
        {'model': 'i10', 'company': 'hyudai', 'price': 5.0},
        {'model': 'fabia', 'company': 'skoda', 'price': 6.5},
        {'model': 'nano', 'company': 'tata', 'price': 1.5}
    ]

    result1 = [car for car in cars if car['price'] <= max]
    print(result1)

    result2 = [car['model'] for car in cars if car['price'] <= max]
    print(result2)

    result3 = [car['company'] for car in cars if car['price'] <= max]
    print(result3)

function5()