#scapping ---> getting computer-like stuff from a web page
#APIs --> you a computer asking another computer for data

#https://darksy.net/dev/account
#https://api.darksky.net/forecast/89ec6e6cc56cb8051d3dbe92cef4647f/37.8267,-122.4233

#endpoint = url

# use the requests library
import requests

url = "https://api.darksky.net/forecast/89ec6e6cc56cb8051d3dbe92cef4647f/37.8267,-122.4233"

response = requests.get(url)

# module : install 
# PIP INSTALL PAGKAGES
# pip3 install requests (in terminal!)

# print(response)

# <Response [200]> means OK!

#print(response.text)
# OR 
#print(response.content)
#dictionaries

# print(response.text.keys())   it didn't work

# print(type(response.text))

# JavaScript Object Notation = json
#print(response.json)

# error: <bound method Response.json of <Response [200]>> 
  #--> means that we lack ()

print(response.json().keys())

# ansewer: dict_keys(['latitude', 'longitude', 'timezone', 'offset', 'currently', 'minutely', 'hourly', 'daily', 'flags'])

data = response.json

#print(type(data)) 
# --> is a dictionary
print(data.keys())

# give me the data you have for the key 'currently'
#print(data['currently'].keys())

# jupiter notebook --> we are running a server

# shift + enter OR "->"" button

# "markdown" to write text and "code" to write code









