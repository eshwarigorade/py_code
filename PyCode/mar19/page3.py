file = open('./temperatures.txt', 'r')

# parser

temperatures = []
lines = file.readlines()
for line in lines:
    tokens = line.split('=')
    hour = tokens[0].replace(' ', '')
    temperature = tokens[1].replace(' ', '').replace('\n', '')
    temperatures.append({'hour': hour, 'temperature': temperature})

print(temperatures)