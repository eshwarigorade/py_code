import urllib3

# url to load
url = 'https://weather.com/en-IN/weather/hourbyhour/l/cc4e93311b537126218a1d9a0dc33295fd3f3d0c8fe0965a4b8eab0fb00e7d39'

# http pool manager -> to manage the connection
http = urllib3.PoolManager()

# send the request
request = http.request('GET', url)

# read the status code of the response
status = request.status
print('status: {}'.format(status))

# get the data from the response
data = request.data
print(data)

