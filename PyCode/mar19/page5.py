from bs4 import BeautifulSoup
import urllib3

def readFile():
    file = open('./weather.html', 'r')
    data = file.read()
    file.close()
    return data

def readResponseFromURL():
    http = urllib3.PoolManager()
    request = http.request('GET', 'https://weather.com/en-IN/weather/hourbyhour/l/cc4e93311b537126218a1d9a0dc33295fd3f3d0c8fe0965a4b8eab0fb00e7d39')
    data = request.data
    return data

def parseResponse(data):
    info = []
    soup = BeautifulSoup(data, 'html.parser')

    table = soup.find('table', {'class': 'twc-table'})
    tbody = table.find('tbody')
    trs =  tbody.find_all('tr')

    for tr in trs:

        # to get the time and day
        tdTime = tr.find('td', {'headers': 'time'})
        time = tdTime.find('span', {'class': 'dsx-date'}).text
        date = tdTime.find('div', {'class': 'hourly-date'}).text


        # description
        tdDescription = tr.find('td', {'headers': 'description'})
        description = tdDescription.find('span').text

        # temperature
        tdTemperature = tr.find('td', {'headers': 'temp'})
        temp = tdTemperature.find('span').text.replace('°', '')

        # humidity
        tdHumidity = tr.find('td', {'headers': 'humidity'})
        humidity = tdHumidity.find('span').find('span').text.replace('%', '')

        # wind
        tdWind = tr.find('td', {'headers': 'wind'})
        wind = tdWind.find('span').text

        info.append({
            'date': date,
            'hour': time,
            'description': description,
            'temperature': temp,
            'humidity': humidity,
            'wind': wind
        })

        # print('time: {}, date: {}, description: {}, temp: {}, humidity: {}, wind: {}'.format(time, date, description, temp, humidity, wind))

    print(info)
    file = open('./data.csv', 'w')
    file.write('date,time,temperature,humidity,wind,description\n')
    for dict in info:
        file.write('{},{},{},{},{},{}\n'.format(
            dict['date'],
            dict['hour'],
            dict['temperature'],
            dict['humidity'],
            dict['wind'],
            dict['description']))

    file.close()

# data = readFile()
data = readResponseFromURL()
parseResponse(data)