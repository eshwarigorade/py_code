def function1():
    num = 10
    print('num = {}'.format(num))

# function1()

# def function2():
#     print('num = {}'.format(num))
#
# function2()

def outerFunction():
    # local
    num = 10
    print('inside outer function')
    print('num = {}'.format(num))

    # local
    def innerFunction():
        print('inside innerFunction')
        print('num = {}'.format(num))
        name = 'steve'
        print('name = {}'.format(name))

    print('name = {}'.format(name))
    innerFunction()

outerFunction()

