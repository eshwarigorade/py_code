import pandas as pd

def function1():
    """
    1 2
    3 4
    """
    df1 = pd.DataFrame([[1, 2], [3, 4]])
    print(df1)

    l1 = [1, 2, 3]
    l2 = [4, 5, 6]
    df2 = pd.DataFrame([l1, l2])
    print(df2)

# function1()

def function2():
    """
        person1     45      pune
        person2     15      karad
    """
    p1 = ['person1', 'pune', 45]
    p2 = ['karad', 'person2', 15]
    df1 = pd.DataFrame([p1, p2])
    print(df1)


function2()

def function3():
    p1 = { 'name': 'person1', 'age': 45, 'address': 'pune' }
    p2 = { 'age': 15, 'address': 'karad', 'name': 'person2' }
    df1 = pd.DataFrame([p1, p2])
    print(df1)

function3()