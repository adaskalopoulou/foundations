# Aspasia Daskalopoulou
# 05/26/2017
# Homework 3
"""
COMMENTS - JAGER HARTMAN

*** Part 1 ***
SCORE: 5/5
 
* Instead of the insert function you can also use the append function to add items to a list

* Counting valeus above/below the mean can be accomplished with one for loop using an else condition

    for number in numbers:
        if number > mean:
            vam += 1
        else:
            vbm += 1

* Try not to use id as a variable name since lowercase id is a built in variable for python


*** Part 2 ***
SCORE: 5/5

* When checking for heat stroke use an else statement.  If the patient has a temperature of 102 exactly
nothing will be printed with your code.


*** Part 3 ***
SCORE: 5/5

* A shorthand for 'x = x + 1' is simply 'x += 1' which can save a lot of typing in the long run
"""

# PART ONE: DICTIONARIES!

###### NUMBERS ######
numbers = [4, 5, 1, 10, 200, 34, 22, 19, 43, 56, 32, 11, 40, 82, 23, 43, 12, 65, 10]

print("1. How many numbers are in the list?")

count_numbers = 0
for number in numbers:
  count_numbers = count_numbers + 1
print(count_numbers, "numbers in the list")

print ("2. Add another number to the list.")

numbers.insert(19, 15)
print(numbers)

print("3. How many even numbers are in the list?")

count_even_numbers = 0
for number in numbers:
  if number % 2 == 0:
    count_even_numbers = count_even_numbers + 1
print(count_even_numbers, "even numbers")

print("4. How many values are above the mean and how many are below the mean?")

#vam= values above mean
count_vam = 0
for number in numbers:
  if number > (sum(numbers)/len(numbers)):
    count_vam = count_vam + 1
print(count_vam, "values above mean")

#vbm= values below mean

count_vbm = 0
for number in numbers:
  if number < (sum(numbers)/len(numbers)):
    count_vbm = count_vbm + 1
print(count_vbm, "values below mean")

print("5. What is the sum of the numbers?")

sum_numbers = 0
for number in numbers:
  sum_numbers = sum_numbers + int(number)
print(sum_numbers, "is the sum of all the numbers")

print("6. What is the sum of the numbers that are above the mean and the numbers below the mean?")
#vam= values above mean

sum_vam = 0 
for number in numbers: 
  if number > (sum(numbers)/len(numbers)):
    sum_vam = sum_vam + int(number)
print(sum_vam, "is the sum of all the numbers that are above the mean")

#vbm= values below mean
sum_vbm = 0 
for number in numbers: 
  if number < (sum(numbers)/len(numbers)):
    sum_vbm = sum_vbm + int(number)
print(sum_vbm, "is the sum of all the numbers that are below the mean")

print("7. Which is the largest number?")

m = 0
for number in numbers:
  if number > m :
    m = number 
print(m, "is the largest number") 

############# DOGS #################

print("8. Add you dog Maxwell to the list.")

dogs = ["Sparky", "Jane", "Matilda", "Blartsburg"]

dogs.insert(1, "Maxwell")
print(dogs)

print("9. List of all dogs that have names of 5 characters or less.")

small = 6 
for dog in dogs: 
  if len(dog) < small:
    print(dog, "is the dog whose name is shorter than 5 characters long")


############# CH website #################

print("10. What is the link for every canton in Switzerland?")

url_ZH = "http://important-swiss-things.ch/docs/download/ZH"
cantons = ["ZH", "BE", "LU", "UR", "SZ", "OW", "NW", "GL", "ZG", "FR", "SO", "BS", "BL", "AR", "AI", "SG", "GR", "AG", "TG", "TI", "VD", "VS", "NE", "GE", "JU"]

for canton in cantons:
  url_ZH.replace("ZH", canton)
  print(url_ZH.replace("ZH", canton))

############# top-secret-secrets.com #################

print("11. Print out all of the URLs from top-secret documents.")

url_qq7lthm_01 = "www.top-secret-pdfs.com/content/secrets/QQ7LTHM/page/001.pdf"
IDs = ["qq7lthm", "jemsqhg", "O6itcke", "cp4Iua0", "bkijcmo", "ctoyjrm", "z8wc6xy", "zk4Bmm0"]
PDFs = ["001", "002", "003", "004", "005", "006", "007", "008", "009", "010", "011", "012"]

for ID in IDs:
  ID = ID.upper()
  for PDF in PDFs:
    print(url_qq7lthm_01.replace("QQ7LTHM", ID).replace("001", PDF)) 


# PART TWO: Dictionaries

############# A DOCTOR TO AVOID #################

# 1. # 2.

patient = {
  'complaint' : 'headaches',
  'heart rate' : 70,
  'temperature' : 98.6,
  'infection' : 'No',
  'diagnosis' : 'You need to relax'

}

print(patient.keys())
print("Doctor, it looks like the patient is complaining about", patient['complaint'])

# 3. 

if patient['heart rate'] > 90 and patient['heart rate'] < 110:
  print(patient['diagnosis'])

if patient['temperature'] > 102:
  if patient['infection'] == 'No':
    print("Your diagnosis is heat stroke.")

if patient['temperature'] > 98.6:
  if patient['infection'] == 'Yes':
    print("Your diagnosis is flu.")

if patient['infection'] == 'Yes':
  if patient['temperature'] < 98.6:
    print("Your diagnosis is cold.")

else:
  print("Take an aspirin and call me in the morning.")


# 4. 

patients = [

{
  'name' : 'Anna',
  'complaint' : 'headaches',
  'heart rate' : 125,
  'temperature' : 99,
  'infection' : 'Yes'
},

{ 
  'name' : 'Lina',
  'complaint' : 'seizures',
  'heart rate' : 65,
  'temperature' : 96.6,
  'infection' : 'Yes'
},

{
  'name' : 'Stephan',
  'complaint' : 'stomach_pain',
  'heart rate' : 85,
  'temperature' : 105,
  'infection' : 'No'
}]


for patient in patients:
  if patient['temperature'] > 102:
    if patient['infection'] == 'No':
      print(patient['name'], "your diagnosis is heat stroke.")
  if patient['temperature'] > 98.6:
    if patient['infection'] == 'Yes':
      print(patient['name'], "your diagnosis is flu.")
  if patient['infection'] == 'Yes':
    if patient['temperature'] < 98.6:
      print(patient['name'], "your diagnosis is cold.")

#else:
  # print(patient['name'], "Take an aspirin and call me in the morning.")

# 5.


temperatures = [ 99, 105, 98, 99, 100, 104, 105, 100 ]

patients = {}
for temperature in temperatures:
  if temperature > 102:
    print("The patient with temperature", temperature, "has a heat stroke")
  if temperature < 102:
    print("The patient with temperature", temperature, "hasn't a heat stroke")



# PART THREE: Reading CSV files
print("Reading CSV files")

import csv
csvfile = open('countries.csv', 'r')
reader = csv.DictReader(csvfile)
data = list(reader)
csvfile.close()

print("1. What are the COLUMNS in our dataset?")

print(reader.fieldnames)

print("2. How many countries do we have in our dataset?")

row_count = sum(1 for row in data)  
print(row_count)

print("3a. How many countries in Asia do we have in our dataset?")

count_asia = 0
for row in data:
  if row['Continent'] == "Asia":
    count_asia = count_asia + 1
print(count_asia)

print("3b. How many countries in South America do we have in our dataset?")

count_same = 0
for row in data:
  if row['Continent'] == "S. America":
    count_same = count_same + 1
print(count_same)

print("4. What is the total population of the world?")

total_pop = 0
for row in data:
  row_pop = int(row['Population'])
  total_pop = total_pop + row_pop
print(total_pop)

print("5. Which has a larger population, Africa or South America?")

afr_pop = 0
for row in data:
  if row['Continent'] == "Africa":
    row_pop = int(row['Population'])
    afr_pop = afr_pop + row_pop

same_pop = 0
for row in data:
  if row['Continent'] == "S. America":
    row_pop = int(row['Population'])
    same_pop = same_pop + row_pop

if afr_pop > same_pop:
  print("Africa has a larger population than South America.")
else:
  print("South America has a larger population than Africa.") 

print("6. Calculate the total GDP of each country.")

for row in data:
  gdp = int(row['Population']) * float(row['GDP_per_capita'])
  print(row['Country'], gdp)

print("7. What is the median life expectancy of the world?")

import statistics as s

row_life =[]

for row in data:
  row_life.append(float(row['life_expectancy']))
print(s.median(row_life))

print("8. What is the median life expectancy of Europe?")

row_life_eu = []

for row in data:
  if row['Continent'] == "Europe":
    row_life_eu.append(float(row['life_expectancy']))
print(s.median(row_life_eu))

print("9. Countries that have a below-average life expectancy.")

row_life =[]

for row in data:
  row_life.append(float(row['life_expectancy']))
  if s.mean(row_life) < float(row['life_expectancy']):
    print(row['Country'])

print("10. Countries that have a below-average GDP but an above-average life expectancy.")

row_gdp = []
row_life =[]

for row in data:
  row_gdp.append(int(row['GDP_per_capita']))
  row_life.append(float(row['life_expectancy']))
  if s.mean(row_gdp) < int(row['GDP_per_capita']):
    if s.mean(row_life) > float(row['life_expectancy']):
      print(row['Country'])

print("11. What is the 75th percentile of GDP is?")

row_gdp = []
row_gdp_up = []

for row in data:
  row_gdp.append(float(row['GDP_per_capita'])) 
  if float(row['GDP_per_capita']) > (s.median(row_gdp)):
    row_gdp_up.append(float(row['GDP_per_capita'])) 
print(s.median(row_gdp_up))


print("12a. What percent of the world population has a life expectancy of below 50 years?")

pop_low_life =[]
row_life = []
total_pop_low_life = 0

for row in data:
  row_life.append(float(row['life_expectancy']))
  if float(row['life_expectancy']) < 50:
    pop_low_life.append(int(row['Population']))
    total_pop_low_life = total_pop_low_life + int(row['Population'])
print(round((total_pop_low_life * 100) / total_pop), "%")

print("12b. What percent of the world population has a life expectancy of below 80 years?")

pop_med_life =[]
row_life = []
total_pop_med_life = 0

for row in data:
  row_life.append(float(row['life_expectancy']))
  if float(row['life_expectancy']) < 80:
    pop_med_life.append(int(row['Population']))
    total_pop_med_life = total_pop_med_life + int(row['Population'])
print(round((total_pop_med_life * 100) / total_pop), "%")




























