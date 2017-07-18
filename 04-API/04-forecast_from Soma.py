# Brand new file
# ALL ABOUT APIS

# https://darksky.net/dev/account
# https://api.darksky.net/forecast/15074402c474e3dab67f7377e1f95519/37.8267,-122.4233

# urllib, urllib2 = BAD
# requests = GOOD

# Say "hey, lets use the requests library"
import requests

url = "https://api.darksky.net/forecast/15074402c474e3dab67f7377e1f95519/37.8267,-122.4233"

# Hey requests, go get that url! And save
# the response as 'response'
response = requests.get(url)
# JavaScript Object Notation = JSON
data = response.json()

print(type(data))

print(data.keys())

# Hey dictionary, give me the data you
# have for the key 'currently'
print(data['currently'])

print(data['currently'].keys())

print(data['currently']['temperature'])

