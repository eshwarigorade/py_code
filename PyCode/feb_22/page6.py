def function1():
    numbers = [1, 2, 3, 4, 5, 3, 4, 5, 2, 1]
    print(type(numbers))
    numbers.append(10)
    print(numbers)

function1()

def function2():
    # mutable
    s1 = {1, 3, 5, 6, 7, 2, 3, 4, 5, 3, 4, 5, 2, 1}
    print(type(s1))
    s1.add(40)
    print(s1)

# function2()

def function3():
    # mutable
    s1 = set([1, 3, 5, 6, 7, 2, 3, 4, 5, 3, 4, 5, 2, 1])
    print(type(s1))
    s1.add(40)
    print(s1)

# function3()

def function4():
    # immutable
    s1 = frozenset([1, 3, 5, 6, 7, 2, 3, 4, 5, 3, 4, 5, 2, 1])
    print(type(s1))
    print(s1)

# function4()

def function5():
    s1 = {1, 2, 3, 4, 5}
    s2 = {4, 5, 6, 7, 8}
    print('s1 U s2 = {}'.format(s1.union(s2)))
    print('s2 U s1 = {}'.format(s2.union(s1)))
    print('s1 intersection s2 = {}'.format(s1.intersection(s2)))
    print('s2 intersection s1 = {}'.format(s2.intersection(s1)))
    print('s1 - s2 = {}'.format(s1 - s2))
    print('s2 - s1 = {}'.format(s2 - s1))


function5()