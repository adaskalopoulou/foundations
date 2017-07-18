# Aspasia Daskalopoulou
# 05/24/2017
# Homework 2, Part 2

# LISTS

#1 
countries = ['Japan', 'Germany', 'Netherlands', 'Switzerland', 'Italy', 'France', 'Belgium']
#2
for country in countries:
  print (country)
# 3
[countries.sort()]
# 4
print (countries[0])
# 5
print (countries[5])
# 6
countries.remove('Japan')
# 7
for country in countries:
  print (country.upper())

# DICTIONARIES

# 1
trees = {
  'name': 'Lost Tree',
  'species' : 'Acacia',
  'age' : 30,
  'location_name' : 'Sahara desert',
  'latitude' : 20.645,
  'longitude' : 11.249
}
# 2
print (trees['name'], "is a", trees['age'], "year old tree that is in", trees['location_name'])

# 3
if trees['latitude'] < 40.7128: 
  print ("The tree", trees['name'], "in", trees['location_name'], "is south of NYC")
else: 
  print ("The tree", trees['name'], "in", trees['location_name'], "is", "north of NYC")

# 4
age = input ("How old are you?")
print (age, "years old")
if int(age) > trees['age']:
  print ("You are", (int(age) - trees['age']), "years older than", trees['name'])
else:
  print ("You are", (trees['age'] - int(age)), "years older than", trees['name'])

# LIST OF DICTIONARIES

# 1 
cities = [
{'name': 'Moscow', 'latitude': 55.7558, 'longitude': 37.6173},
{'name': 'Tehran', 'latitude': 35.6892, 'longitude': 51.3890},
{'name': 'Falkland Islands', 'latitude': -51.7963, 'longitude': -59.5236},
{'name': 'Seoul', 'latitude': 37.5665, 'longitude': 126.9780},
{'name': 'Santiago', 'latitude': -33.4489, 'longitude': -70.6693}
]
# 2 
print ("List of cities above or below the equator:")
for city in cities:
  print (city['name'])
  if city['latitude'] > 0:
    print ("the city is above the equator")
  else:
    print ("the city is below the equator")
  if city['name'] =='Falkland Islands':
    print ("The Falkland Islands are a biogeographical part of the mild Antarctic zone")

# 3
print ("List of cities above or below the coordinates of", trees['name'])
for city in cities:
  print (city['name'])
  if city['latitude'] > trees['latitude']:
    print ("the city is north of", trees['name'])
  else:
    print ("the city is south of", trees['name'])


