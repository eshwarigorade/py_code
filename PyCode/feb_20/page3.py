# void function1();
# void function1(int num) {
#  printf("inside function");
#      printf("inside function too");
# }
# printf("inside function too");

# declaring a parameterless function
def function1():
    print("inside function")
    print("inside function too")

    # calling function
    # function1()

# function1()

# void function2(int num) {}
# function2(100)

# empty function
# void function3() {}
def function3():
    pass

# parameterized function
def function2(num):
    print(num)
    print(type(num))

# function2(100) # int
# function2(4.5) # float
# function2("test") # str
# function2(True) # bool

# int num = 10;
# num: Int = 10;

def addNumbers(num1, num2):
    """
    this function is a very simple function used
    to add two numbers
    """
    answer = num1 + num2
    print(answer)

print(addNumbers.__doc__)
# addNumbers(10, 20)
print(function2.__doc__)