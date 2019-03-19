def function1():
    value = "10"
    print("value in string = {}, {}".format(value, type(value)))

    # type cast string to int
    numberFloat = int(value)
    print("value in int = {}, {}".format(numberFloat, type(numberFloat)))

    # type cast string to float
    numberFloat = float(value)
    print("value in int = {}, {}".format(numberFloat, type(numberFloat)))

# function1()

def function2():
    number = 10
    # print("value in int = {}, {}".format(number, type(number)))
    print("number = " + str(number))

    # convert int to string
    numberStr = str(number)
    print("value in string = {}, {}".format(numberStr, type(numberStr)))

# function2()


def function3():
    value = '10.5'

    print('isalpha = {}'.format(value.isalpha()))
    print('isalnum = {}'.format(value.isalnum()))
    print('isnumeric = {}'.format(value.isnumeric()))

    if value.isnumeric():
        number = int(value)
        print('number = {}'.format(number))
    else:
        print('error.. you have entered a wrong number value')

# function3()






















