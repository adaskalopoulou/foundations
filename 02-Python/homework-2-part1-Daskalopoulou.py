# Aspasia Daskalopoulou
# 05/24/2017
# Homework 2, Part 1

# A. LISTS

#1
numbers = [22, 90, 0, -10, 3, 22, 48]
# 2
print (len(numbers), "is the number of elements in the list")
# 3
print (numbers[3], "is the 4th element of this list")
# 4
print (numbers[1] + numbers[3], "is the sum of the 2nd and 4th element of the list")
# 5
numbers.remove(max(numbers))
print (max(numbers), "is the 2nd-largest value in the list")
# 6
numbers = [22, 90, 0, -10, 3, 22, 48]
print (numbers[6], "is the last element of the original unsorted list")
# 7
for number in numbers:
  if int(number) < 10:
    print(int(number) * 30, "when", (number), "is multiplied by thirty")
    if (int(number) % 2 == 0):
      print((int(number) * 30) + int(6), "when I add 6 to an even number multiplied by thirty")
  if int(number) > 50:
    print (int(number) - int(10), "if greater than 50 and when we subtract 10")
  if int(number) != -10:
    print((int(number) * 30) + int(6) - 1, "if the number is not -10 and when we subtract 1")
#8
print (sum(numbers) / 2, "is the sum of all of the numbers divided by two")
  
# B. Dictionaries

# 8
movie = {
  'title': 'Hello',
  'year' : '1960',
  'director' : 'Aspasia'
}
print ("My favorite movie is", movie['title'], "which was released in", movie['year'], "and was directed by", movie['director'])

# 9
movie = {
  'title': 'Hello',
  'year' : '1960',
  'director' : 'Aspasia',
  'budget' : 100000,
  'revenue' : 500000
}
print ("The difference between revenue and budget is", int(movie['revenue']) - int(movie['budget']))
# 10
if int(movie['revenue']) - int(movie['budget']) < 0:
  print ("It was a flop")
if int(movie['revenue']) >= 5 * int(movie['budget']):
  print ("That was a good investment")

# NEW DICTIONARY  
# 11

borough1 = {
  'name' : 'Manhattan',
  'residents' : 1.6 
}
borough2 = {
  'name' : 'Brooklyn',
  'residents' : 2.6 
}
borough3 = {
  'name' : 'Bronx',
  'residents' : 1.4 
}
borough4 = {
  'name' : 'Queens',
  'residents' : 2.3 
}
borough5 = {
  'name' : 'Staten Island',
  'residents' : 0.47 
}

# 1
print (borough2['residents'], "is the population of Brooklyn")

# 13 
print (borough1['residents'] + borough2['residents'] + borough3['residents'] + borough4['residents'] + borough5['residents'], "million residents in all 5 boroughs")

# 14
print (round(((borough1['residents']) / (borough1['residents'] + borough2['residents'] + borough3['residents'] + borough4['residents'] + borough5['residents'])) * 100), "% of of NYC's population lives in Manhattan")

