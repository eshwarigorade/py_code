def log(func):
    def inner(*args, **kwargs):
        print('inside log')
        print('function: {}'.format(func))
        print(args, kwargs)
        func(*args, **kwargs)
    return inner

@log
def add(p1, p2):
    print('p1 + p2 = {}'.format(p1 + p2))

@log
def multiply(p1, p2):
    print('p1 * p2 = {}'.format(p1 * p2))

@log
def square(p1):
    print('square of p1 = {}'.format(p1 * p1))

@log
def cube(p1):
    print('cube of p1 = {}'.format(p1 * p1 * p1))

add('10', 20)
# multiply(20, 40)
# square(34)
# cube(5)