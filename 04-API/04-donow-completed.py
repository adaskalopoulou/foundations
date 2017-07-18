# Do Now
# Wednesday, May 31, 2017

# Reviewing: dictionaries, lists, for loops

# 1) I have a list called bubblegum. How do I get the first element? The last element?

bubblegum = [5, 4, 3, 10, 12]

print(bubblegum)
print(bubblegum[0])
print(bubblegum[3])
print(bubblegum[-1])
print(bubblegum[-2])

# 2) What function or method…
#  …tells how many elements are in a list?

print(len(bubblegum))

#  …replaces text in a string with other text?
print("HELLO".replace("L", "E"))
print("dogs r cool".replace("dogs", "cats"))

#  …gives you the keys of a dictionary?

something = {
  'blah': 'something',
  'blee': 5
}
something['another_key'] = 3000000

print(something.keys())

print(something.values())

# 3) What is the output of the following code? Which lines give you errors?

# borough_name = 'Manhattan'
# z = [ 'Manhattan', 'Queens' ]
# x = { 'borough_name': 'Manhattan', 'population': 500 }
# y = {
#   'Manhattan': 500,
#   'Queens': 200
# }

# print x['borough_name']
# print x[borough_name]
# print x[0]
# print y['borough_name']
# print y[borough_name]
# print y[0]
# print z['borough_name']
# print z[borough_name]
# print z[0]

# 4)  Print out each art piece’s name. 
art_pieces = [
  { 'title': 'Gold Star', 'year': 1805 }, 
  { 'title': 'Blunderbuss', 'year': 1800 },
  { 'title': 'Chairlift', 'year': 1976 },
  { 'title': 'Rancor', 'year': 2002 }
]

for piece in art_pieces:
  print(piece['title'])

# 5) Given the following, write code to calculate how many murders we have in total.

murders = { 
  'Albany': 23, 
  'Kings County': 10, 
  'Rochester': 7, 
  'Yonkers': 9
}

total = murders['Albany'] + murders['Kings County'] + murders['Rochester'] + murders['Yonkers']
print(total)

list_of_murder_numbers = [23, 10, 7, 9]
print(sum(list_of_murder_numbers))

print(murders.values())
print(sum(murders.values()))


cities = [
  { 'name': 'Albany', 'murders': 400 },
  { 'name': 'NYC', 'murders': 20 },
  { 'name': 'Rochester', 'murders': 123 }
]

# Start with knowing about zero murders
total = 0

for city in cities:
  print("I found", city['murders'], "murders")
  total = total + city['murders']

print("Total is", total, "murders")

murder_list = []
for city in cities:
  murder_list.append(city['murders'])
  print("I've found", murder_list, "so far")
print("My total list is", murder_list)
print(sum(murder_list))


murders = [city['murders'] for city in cities]
print("I have found:", murders)

names = [city['name'] for city in cities]
print("I have found:", names)


numbers = [3, 6, 4, 1, 10, 30]
# Make a new list, with each element
# being 100 times larger than the original
# using the MAGIC of list comprehensions

for number in numbers:
  print(number * 100)

big_numbers = [num * 100 for num in numbers]
print(big_numbers)


cities = [
  { 'name': 'Albany', 'murders': 400, 'pop': 800 },
  { 'name': 'NYC', 'murders': 20, 'pop': 1000 },
  { 'name': 'Rochester', 'murders': 123, 'pop': 250 }
]

pct_killed = [round(city['murders'] / city['pop'] * 100) for city in cities]
print(pct_killed)


# 400
# 20
# 123

total = 0
total = total + 400
total = total + 20
print("I know about", total, "murders")

cats = [1, 2, 3, 4, 5]
dogs = [6, 7, 8, 9, 10]

for cat, dog in zip(cats, dogs):
  print(cat, dog)


