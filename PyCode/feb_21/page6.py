def function1():
    numbers1 = [1, 2, 3, 4, 5]
    print(numbers1)
    print('type of numbers1: {}'.format(type(numbers1)))

    numbers2 = (1, 2, 3, 4, 5)
    print(numbers2)
    print('type of numbers2: {}'.format(type(numbers2)))

# function1()

def function2():
    t1 = (1, 2, 3, 4, 5)

    for value in t1:
        print(value)

# function2()

def function3(*arguments):
    print(arguments)
    print(type(arguments))

# function3(10)
# function3(10, 20)
# function3(10, 20, 30)
# function3(10, 20, 30, 40)

def add(*arguments):
    answer = 0
    for value in arguments:
        answer += value

    print("answer = {}".format(answer))

add(10, 20)
add(10, 20, 30)
add(10, 20, 30, 40)
add(10, 20, 30, 40, 50)
add(10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50)

# print(int('ten'))

