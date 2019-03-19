from bs4 import BeautifulSoup

# read the file
file = open('./hello.html', 'r')
data = file.read()

# create a soup
soup = BeautifulSoup(data, 'html.parser')

# h1 = soup.find('h1')
# print(h1)
# print(h1.text)

# h2 = soup.find('h2')
# print(h2)
# print(h2.text)

# divs = soup.find_all('div')
# for div in divs:
#     print(div.text)

# divs = soup.find_all('div', {'class': 'temp'})
# for div in divs:
#     print(div.text)


data = []
divsInfo = soup.find_all('div', {'headers': 'info'})
for divInfo in divsInfo:
    divTime = divInfo.find('div', {'class': 'hourly-time'})
    # print(divTime.text)
    divDate = divInfo.find('div', {'class': 'hourly-date'})
    # print(divDate.text)
    data.append({'time': divTime.text, 'day': divDate.text})

print(data)

