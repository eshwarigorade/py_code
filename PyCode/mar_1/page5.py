class InvalidAgeException(Exception):
    pass

class InvalidSalaryException(Exception):
    pass

def function1(p1, p2):
    try:
        age = int(input('your age: '))
        if age < 20 or age > 60:
            raise InvalidAgeException('invalid age')
    except InvalidAgeException:
        print('invalid age in function1')

    try:
        salary = int(input('your salary: '))
        if salary < 10 or salary > 30:
            raise InvalidSalaryException('invalid salary')
    except InvalidSalaryException:
        print('invalid salary in function1')

    try:
        result = p1 / p2
        print('result: {}'.format(result))
    except ZeroDivisionError:
        print('division by zero')

function1(20, 0)

# try:
#     function1(10, 0)
# except InvalidAgeException:
#     print('invalid age exception occurred')
# except InvalidSalaryException:
#     print('invalid salary exception occurred')
# except:
#     print('all the remaining exceptions will be handled here')
