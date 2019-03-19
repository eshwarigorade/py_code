def decorate(func):
    def inner(*args, **kwargs):
        print('---------------')
        func(*args, **kwargs)
        print('---------------')

    return inner

@decorate
def multiply():
    p1 = 100
    p2 = 20
    print('p1 * p2 = {}'.format(p1 * p2))

@decorate
def substract():
    p1 = 100
    p2 = 20
    print('p1 - p2 = {}'.format(p1 - p2))

# multiply()
# result = decorate(multiply)
# result()

# substract()

@decorate
def add(p1, p2):
    print('p1 + p2 = {}'.format(p1 + p2))


add(10, 20)
add(p1=10, p2=20)
add(10, p2=30)

def add2(*args, **kwargs):
    print(args)
    print(kwargs)

# add2(10, 20, 30, 40)
# add2(p1=10, p2=20)
# add2(10, 20, p1 = 200, p2 = 400)