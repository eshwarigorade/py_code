file = open('./file1.txt', 'r')

# data = file.read()
# print(data)

# read the data line by line
lines = file.readlines()

for line in lines:
    words = line.split(' ')
    print(words)
