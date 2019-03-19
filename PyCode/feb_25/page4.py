
def execute(p1, p2):
    def add(p1, p2):
        return p1 + p2

    def multiply(p1, p2):
        return p1 * p2

    addition = add(p1, p2)
    multiplication = multiply(p1, p2)
    return (addition, multiplication)

# result = execute(10, 20)
# print(result)


# closure
def execute2(p1, p2):
    def add():
        return p1 + p2

    return add

# result = execute2(10, 20)
# print(result)
# result2 = result()
# print(result2)


# closure
def execute3(p1, p2):
    def multiply():
        return p1 * p2
    return multiply

# result = execute3(30, 50)
# print(result())


def execute4(p1, p2):
    def add():
        return p1 + p2
    
    def divide():
        return p1 / p2
    return divide

result = execute4(100, 20)
print(result())

















