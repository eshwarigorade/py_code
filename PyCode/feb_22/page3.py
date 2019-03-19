# global
num = 100
print('outside of any function num = {}'.format(num))


def function1():
    # do not declare  a local variable
    global num
    num = 200
    print('inside function1')
    print('num = {}'.format(num))

function1()

print('outside of any function num = {}'.format(num))
