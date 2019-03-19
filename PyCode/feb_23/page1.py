def function1():
    print('inside function1')

# function1()

# # function alias
myFunction1 = function1

# myFunction1()

num = 100
# num2 = num

def function2(p1):
    # p1 = num
    print('inside function2')
    print(type(p1))
    p1()

# function2(10)
# function2('10')
# function2(True)
# function2(num)
# function2(myFunction1)

def function3(f1):
    # function alias
    # f1 = function4
    print('inside function3')
    print(type(f1))
    f1()

# function3(myFunction1)

# var of function4
def function4():
    print('inside function4')

# myFunction4 = function4

# function3(myFunction4)
function3(function4)