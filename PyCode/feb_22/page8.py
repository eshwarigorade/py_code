num1 = 20
# print(type(num1))  # int
# print(num1)        # 20

# num2 will have the value of num1
num2 = num1

def function1():
    print('inside function1()')

# function1()
# print(type(function1))
# print(function1)

# alias (second name) of function
myFunction1 = function1

function1()
myFunction1()

