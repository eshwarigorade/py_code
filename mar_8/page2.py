import pandas as pd

def function1():
    s1 = pd.Series((10, 20, 30, 40, 50))
    print(s1[1])
    print(s1 + 100)
    print(s1 / 100)
    print(s1 - 100)
    print(s1 * 100)

# function1()

def function2():
    s1 = pd.Series((10, 20, 30, 40, 50))
    print(s1 > 20)
    print(s1 < 20)
    print(s1 >= 20)
    print(s1 <= 20)
    print(s1 != 20)
    print(s1 == 20)

# function2()

def function3():
    # s1 = c(10, 20, 30, 40, 50)
    s1 = pd.Series((10, 20, 30, 40, 50))
    print(s1[1])
    print(s1[s1 > 30])
    print(s1[s1 <= 30])

# function3()

def function4():
    s1 = pd.Series(('India', 'USA', 'UK', 'India'))
    print(s1)
    print(s1[s1 == 'India'])

# function4()

def function5():
    models = ('i20', 'nano', 'fortuner', 'compass', 'fabia')
    companies = ('hyundai', 'tata', 'toyota', 'jeep', 'skoda')

    s1 = pd.Series(models)
    s2 = pd.Series(companies)

    # print(s1)
    # print(s2)

    s3 = pd.Series(companies, index=models)
    print(s3)
    print(s3['compass'])

    s4 = pd.Series(models, index=companies)
    print(s4)
    print(s4['tata'])


# function5()


def function6():
    d1 = { 'i20': 'hyundai', 'nano': 'tata' }
    s1 = pd.Series(d1)
    print(s1)
    print(s1['i20'])

    d2 = { 'hyundai': 'i20', 'tata': 'nano' }
    s2 = pd.Series(d2)
    print(s2)
    print(s2['hyundai'])

function6()
