# empty function
def function1():
    pass

# parameterless function
def function2():
    print("inside function2")

# function2()

# parameterized function
def function3(num):
    print(num)
    print(type(num))

# function3(100)
# function3("test")

# void function4(int p1, int p2)  {}
# function4(10);
# default value
def function4(p1 = 40, p2 = 30):
    """
    parameterized function
    """
    print("p1 = {}".format(p1))
    print("p2 = {}".format(p2))

# function4(10, 20)
# function4(10)
# function4(100, 40)
# function4()
# function4(p2="test")


def function5(p2, p1 = 10, p3 = 40, p4 = 60):
    print("p1 = {}".format(p1))
    print("p2 = {}".format(p2))
    print("p3 = {}".format(p3))
    print("p4 = {}".format(p4))
    # print("p1 = ", p1)
    # print("p1 = " + str(p1))

# function5(40)
# function5(10, 60)
# function5(40, 50, 60, p4=70)

def function6(p1, p2):
    print("p1 = {}".format(p1))
    print("p2 = {}".format(p2))

# function6(10, 20)
# function6(p1=10, p2=20)
# function6(p2=20, p1=10)
# function6(10, 20, 30, 40, 50, 60, 70, 80)

def calculateInterest(principle, duration, rate=10.5):
    # principle = 10000
    # duration  = 24
    # rate      = 10.5
    print("pinciple: {}".format(principle))
    print("duration: {}".format(duration))
    print("rate: {}".format(rate))

# calculateInterest(10000, 24, 10.6)
# calculateInterest(10000, 24)
# calculateInterest(duration=24, principle=10000)

def canVote(age = 18):
    if age >= 18:
        print("yes.. this person can vote :)")
    else:
        print("no.. this person can NOT vote :(")

# canVote(10)
# canVote(30)

def printGrade(marks):
    """
    grade = A => marks > 80
    grade = B => marks > 60
    grade = C => marks > 40
    grade = F => marks < 40
    """
    if marks < 40:
        print("Grade = F :(:(:(")
    elif marks < 60:
        print("Grade = C :(:(")
    elif marks < 80:
        print("Grade = B :(")
    else:
        print("Grade = A :) :) :)")


printGrade(90)
printGrade(70)
printGrade(50)
printGrade(30)