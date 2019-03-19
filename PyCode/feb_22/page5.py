def function1():
    numbers = [1, 2, 3, 4, 5]
    print(numbers)

    for number in numbers:
        print(number)

# function1()

def function2():
    # matrix = [10, 20, 30, 40]

    # collection of collections
    # matrix = 2x2
    matrix = [
        [10, 20],   # 0
        [30, 40]    # 1
    ]

    # print(matrix[0][0])
    # print(matrix[0][1])
    # print(matrix[1][0])
    # print(matrix[1][1])

    for row in matrix:
        for value in row:
            print(value)

# function2()

# printf("hello world\n");
# printf("hello world");
def function3():
    matrix = [
        [10, 20, 30],
        [40, 50, 60]
    ]

    for row in matrix:
        for value in row:
            print(value, end='|')
        print('')

# function3()

def function4():
    products = [
        ['product1', 20, 100, 'best product?'],
        ['product2', 40, 10, 'another best product?'],
        ['product3', 60, 1, 'another best product?']
    ]

    for product in products:
        for info in product:
            print(info, end=' ')
        print('')

function4()