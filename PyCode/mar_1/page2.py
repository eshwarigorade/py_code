numbers = [11, 24, 38, 46, 53]
value = 4
isEqual = False
for number in numbers:
    if value == number:
        isEqual = True
        break

print('is {} present in numbers: {}'.format(value, isEqual))
print('is {} present in numbers: {}'.format(value, value in numbers))

str1 = "hello"
print('o is in the hello: {}'.format('o' in str1))
print('x is in the hello: {}'.format('x' in str1))
print('llo is in the hello: {}'.format('llo' in str1))
print('llx is in the hello: {}'.format('llx' in str1))

world = ["India", "USA", "UK", "Bhutan"]
print('India is in countries: {}'.format('India' in world))
print('Austrialia is in countries: {}'.format('Austrialia' in world))

l1 = [(1, 2), (3, 4,), (5, 6)]
print('(1, 2) inside l1: {}'.format((1, 2) in l1))
print('1 inside l1: {}'.format(1 in l1))

l2 = [1, 2, 3, 4, 5]
l3 = [3, 4]
