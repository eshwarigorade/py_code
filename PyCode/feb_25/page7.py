# closure
def execute(func):
    def inner():
        print('------------------')
        func()
        print('------------------')
    return inner

@execute
def myFunction():
    print('inside myFunction')

myFunction()
# execute(myFunction)


