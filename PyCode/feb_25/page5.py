def add(p1, p2):
    print('p1 + p2 = {}'.format(p1 + p2))

def multiply(p1, p2):
    print('p1 * p2 = {}'.format(p1 * p2))

def divide(p1, p2):
    print('p1 / p2 = {}'.format(p1 / p2))

def execute(func, p1, p2):
    print('------------------------')
    func(p1, p2)
    print('------------------------')

# add(10, 20)
# multiply(40, 50)
# divide(20, 4)

execute(add, 10, 20)
execute(multiply, 40, 50)
execute(divide, 20, 4)