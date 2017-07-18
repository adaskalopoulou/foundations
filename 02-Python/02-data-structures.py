#
# May 24, 2017: Data Structure
#

# Nothing in here yet...
# But eventually: lists and dictionaries!

# We know about strings
name = "Soma"
home = "Brooklyn"
# We know about integers
age = 34

print("Hello my name is", name, "and I live in", home, "and I am", age, "years old")



friend_name = "Jen"
friend_home = "Brooklyn"
friend_age = 33

print("I have a friend named", friend_name)
print("She lives in", friend_home)
print("And she is", friend_age, "years old")


# Instead of thinking of these as all being separate
# Maybe it's more like, you're a PERSON with
# certain attributes - name, home, age, etc

# These are called dictionaries
myself = {
  'name': 'Soma',
  'age': 34,
  'home': 'Brooklyn'
}

friend = {
  'name': 'Jen',
  'age': 33,
  'home': 'Brooklyn'
}

print (myself)
print (myself['name'])
print ("My name is", myself['name'])

#######################
cat1_age = 7
cat2_age = 9
cat3_age = 2

# this is called a list, or ARRAY

cat_ages = [7, 9, 2]
print (cat_ages)

# list a whole lot of the same things
# but if you have one thing that has different attributes this is a dictionary
#1 list [] square brackets 
#2 dictionary {} curly brases 
#3 list of dictionaries 
#4 list of lists

print (sum(cat_ages))
print ("We have", 3, "cat ages")

# to find the number of elements in a list
print ("We have", len(cat_ages), "cat ages")

experience = [0, 1, 2, 3, 0, 5, 6, 7, 10]
print (len(experience))
# to count how many people in the class have 0 years of experience:
print (experience.count(0))

# Technically speaking
# len is a function, so it comes outside
# .count is a method, so it comes after

cat1_name = "Smushface"
cat2_name = "Boy Abby"
cat3_name = "Triples" 

cats = ["Smushface", "Boy Abby", "Triples"]
print (cats)

# loop!!!!!!!!!!!!!!!!!!!!!
# a FOR LOOP
		# do something to every single element of the list

for cat in cats:
	# print out the cat's name with excitement!
	print (cat, "!!!!!")

# this is the short way:
cat = cats[0]
print (cats[0])
cat = cats[1]

for cat in cats:
# if you want to UPPERCASE the cat's name
	print (cat.upper(), "!!!!!")


experience = [0, 1, 2, 3, 0, 5, 6, 7, 10]
print (len(experience))
# to count how many people in the class have 0 years of experience:
print (experience.count(0))

for years in experience:
	print ("someone has", years, "experience")

# if you only want just one of the elements of the list
cats = ["Smushface", "Boy Abby", "Triples"]
print (cats[0])
# prints out the first cat
print (cats[2])


#########################
#DICTIONARY

myself = {
  'name': 'Soma',
  'age': 34,
  'home': 'Brooklyn'
}

friend = {
  'name': 'Jen',
  'age': 33,
  'home': 'Brooklyn'
}

# FOR LOOP is to go everysingle one of the elements

for something in myself:
	print (something)
# opens up all of the keys... YOU NEVER WANT TO DO THIS! 

##############
experience = [0, 1, 2, 3, 0, 5, 6, 7, 10]
print (len(experience))
# to count how many people in the class have 0 years of experience:
print (experience.count(0))
# len() counts the number of elements in a list
print (len(experience), "total studnets")
# sum() adds them all up
print (sum(experience),"total years")
# gets the maximum
print (max(experience))
# gets the minimum
print (min(experience))


#####!!!!!!!! max-min-average!!!
print (sum(experience) / len(experience)) 

# bring a new tool to do our job
import statistics
# statistics comes with Python,, statistics is a package: module, library, etc
# and then say the new took to find the mean!
exp_mean = statistics.mean(experience)
print (exp_mean, "mean years of experience")

exp_median = statistics.median(experience)
print (exp_median, "median years of experience")

print (sorted(experience))

# if you can find the library to do your job is better than writing your own! 


###############
# How to download a webpage in python
# best answer 
# requests
# BeatifulSoup helps you read webpages as a computer (used for scraping)





