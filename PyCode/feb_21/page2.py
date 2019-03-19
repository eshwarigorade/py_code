def function1():
    # list of integers
    numbers = [10, 20, 30, 40, 50]

    # type = list
    print(type(numbers))

    # [10, 20, 30, 40, 50]
    print(numbers)

    # traditional for-loop
    # int index = 0;
    # for (index = 0; index < 5; index++) {
    #   int value = numbers[index];
    #   printf("value = %d", value);
    # }


    # for..in loop
    # for number in numbers:
    #     print("value = {}".format(number))

    # similar to traditional for..in
    # indices = [2, 3, 4]
    # for index in indices:
    #     value = numbers[index]
    #     print("value = {}".format(value))


# function1()

def function2():
    # list of strings
    countries = ["India", "USA", "UK", "Japan", "Bhutan"]

    # print(countries)

    for country in countries:
        print("country = {}".format(country))

# function2()

def function3():
    # int array[5] =  { 1, 2, 3, 4, 5 };
    list1 = [1, "India", 2, "USA", 3, "UK", True, False, 4, 5, 40.5, "Bhutan"]

    for value in list1:
        print("value = {} {}".format(value, type(value)))

function3()
