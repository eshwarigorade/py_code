def divide(p1, p2):
    try:
        result = p1 / p2
        print('p1 / p2 = {}'.format(result))
    except:
        print('the code has got an exception')

# divide(10, 2)
# divide(10, 0)
# print('after divide(10, 0)')

def function1():
    name = input('your name: ')
    age = int(input('your age: '))
    try:
        if age < 20 or age > 60:
            # print('enter valid age between 20 and 60')
            raise Exception('enter valid age between 20 and 60')
        print('name: {}, age: {}'.format(name, age))
    except:
        print('age exception occurred')

# function1()

def function2():
    age = int(input('your age: '))
    if age < 20 or age > 60:
        raise Exception('invalid age')
    salary = int(input('your salary: '))
    if salary < 10 or salary > 30:
        raise Exception('invalid salary')

try:
    function2()
except:
    print('exception occurred')

# function2()


def function3():
    function2()
    # try:
    #     function2()
    # except:
    #     print('exception occurred and handled in function3')

try:
    function3()
except:
    print('exception occurred and handled in main')



