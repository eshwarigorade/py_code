# variable length argument function
def add(*numbers):
    # print(numbers)
    result = 0
    for number in numbers:
        result += number
    print('result = {}'.format(result))

# add(10, 20)
# add(1, 3, 6, 9)
# add(1, 3, 6, 9, 1, 3, 6, 9, 1, 3, 6, 9)

def add2(arguments):
    result = 0
    for number in arguments:
        result += number
    # print('result = {}'.format(result))
    print('result = ' + str(result))

# add2((10, 20, 30, 40))
# add2((10, 20))

# printf("hello world");
# printf("hello world %d %d %d", p1, p2, p3);
def add3(p1, p2, *args):
    print(p1)
    print(p2)
    print(args)

add3(10, 20)
add3(10, 20, 30, 40, 50)
