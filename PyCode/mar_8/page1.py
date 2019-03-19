import numpy as np
import pandas as pd

def function1():
    """
    series using a list
    """
    series1 = pd.Series([10, 20, 30, 40, 50])
    print(series1)
    # print(series1.dtype)
    # print(series1.shape)
    # print(series1.itemsize)
    # print(series1.size)
    # print(series1.ndim)
    print(series1.values)
    print(series1.index)


# function1()

def function2():
    series1 = pd.Series((10, 20, 30, 40, 50))
    print(series1)
    print(series1.values)
    print(series1.index)

# function2()

def function3():
    """
    series CAN NOT be created with SET
    :return:
    """
    series1 = pd.Series({ 10, 20, 30, 40, 50, 10, 20, 30 })
    print(series1)
    print(series1.values)
    print(series1.index)

# function3()

def function4():
    series1 = pd.Series({ 'name': 'person1', 'email': 'p1@test.com', 'phone': '+912234' })
    print(series1)
    print(series1.values)
    print(series1.index)

function4()