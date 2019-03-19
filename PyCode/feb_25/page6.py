def decorateResult(func):
    def inner():
        print('------------------------')
        func()
        print('------------------------')

    return inner

@decorateResult
def add():
    p1 = 10
    p2 = 20
    print('p1 + p2 = {}'.format(p1 + p2))

@decorateResult
def multiply():
    p1 = 10
    p2 = 20
    print('p1 * p2 = {}'.format(p1 * p2))

@decorateResult
def divide():
    p1 = 10
    p2 = 20
    print('p1 / p2 = {}'.format(p1 / p2))

add()
multiply()
divide()

# result = decorateResult(add)
# result()

# result = decorateResult(multiply)
# result()
