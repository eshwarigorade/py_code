def function1():
    myRange = range(0, 11)
    print(myRange)
    numbers = list(myRange)
    print(numbers)

# function1()

def function2():
    numbers = list(range(0, 10))
    print(numbers)

    numbers2 = list(range(0, 10, 2))
    print(numbers2)

# function2()

def function3():
    # int numbers[5] = [10, 20, 30, 40, 50]
    numbers = [10, 20, 30, 40, 50, 60]
    print(numbers)

    # get the length/count of a list
    print("length of numbers: {}".format(len(numbers)))

    # append a new value in the numbers
    numbers.append(70)
    print(numbers)

    # remove the last element
    lastValue = numbers.pop()
    print("last value: {}".format(lastValue))
    print(numbers)

    # add value at a specific index
    numbers.insert(1, 100)
    print(numbers)

    # remove in between value
    numbers.remove(40)
    print(numbers)

    # sort the list
    # numbers.sort()
    # print(numbers)
    #
    # numbers.sort(reverse=True)
    # print(numbers)

    # reverse the list
    numbers.reverse()
    print(numbers)

    # update the value
    numbers[1] = 500
    print(numbers)


function3()