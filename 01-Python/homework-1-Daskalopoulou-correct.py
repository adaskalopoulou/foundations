#Aspasia Daskalopoulou
#05/22/2017
#Homework 1
date = input ("What is your year of birth?")
print (date)
age = 2017 - int(date)
print (int(age), "Age")
print (int(age) * 42000000, "Human Heartbeats")
print (int(age) * 4730400, "Blue Whale Hearbeats")
print (int(age) * 70956000, "Rabbit Hearbeats")
if (int(age) * 70956000) > 1000000000:
	print (round((int(age) * 70956000) / 1000000000), "Billion", "Rabbit Heartbeats")
days = (int(age) * 365)
print (round(int(days) / 225), "Venus years")
print (round((int(age) / 164),1), "Neptune years")
if int(age) > 34:
	print ("Older")
	print (int(age) - 34)
if int(age)< 34:
	print ("Younger")
	print (34 - int(age))
if int(age) == 34:
	print ("Same age")
if (int(date) % 2 == 0):
	print ("Even")
else: print ("Odd")
if int(date) < 1975:
	print (6, "Pittsburgh Steelers' Superbowl championships")  
if 1974 < int(date) < 1976:
	print (5, "Pittsburgh Steelers' Superbowl championships")
if 1975 < int(date) < 1979:
	print (4, "Pittsburgh Steelers' Superbowl championships")
if 1978 < int(date) < 2005:
	print (3, "Pittsburgh Steelers' Superbowl championships")
if 2004 < int(date) < 2006:
	print (2, "Pittsburgh Steelers' Superbowl championships")
if 2005 < int(date) < 2009:
	print (1, "Pittsburgh Steelers' Superbowl championships")
if int(date) > 2008:
	print (0, "Pittsburgh Steelers' Superbowl championships")
if 1934 < int(date) < 1945:
	print ("Franklin D. Roosevelt")
if int(date) == 1945:
	print ("Franklin D. Roosevelt or Harry S. Truman was US President")
if 1945 < int(date) < 1953:
	print ("Harry S. Truman was the US President")
if int(date) == 1953:
	print ("Harry S. Truman or Dwight Eisenhower was US President")
if 1953 < int(date) < 1961:
	print ("Dwight Eisenhower was the US President")
if int(date) == 1961: 
	print ("Dwight Eisenhower or John F. Kennedy was US President")
if 1961 < int(date) < 1963:
	print ("John F. Kennedy was the US President")
if int(date) == 1963:
	print ("John F. Kennedy or Lyndon Johnson was US President")
if 1963 < int(date) < 1969:
	print ("Lyndon Johnson was the US President")
if int(date) == 1969:
	print ("Lyndon Johnson or Richard Nixon was US President")
if 1969 < int(date) < 1974:
	print ("Richard Nixon was US President")
if int(date) == 1974:
	print ("Richard Nixon or Gerald Ford was US President")
if 1974 < int(date) < 1977:
	print ("Gerald Ford was US President")
if int(date) == 1977:
	print ("Gerald Ford or Jimmy Carter was US President")
if 1977 < int(date) < 1981:
	print ("Jimmy Carter was US President")
if int(date) == 1981:
	print ("Jimmy Carter or Ronald Reagan was US President")
if 1981 < int(date) < 1989:
	print ("Ronald Reagan was US President")
if int(date) == 1989:
	print ("Ronald Reagan or George H. W. Bush was US President")
if 1989 < int(date) < 1993:
	print ("George H. W. Bush was US President")
if int(date) == 1993:
	print ("George H. W. Bush or William J. Clinton was US President")
if 1993 < int(date) < 2001:
	pring ("William J. Clinton was US President")
if int(date) == 2001:
	print ("William J. Clinton or George W. Bush was US President")
if 2001 < int(date) < 2009:
	print ("George W. Bush was US President")
if int(date) == 2009:
	print ("George W. Bush or Barack Obama was US President")
if 2009 < int(date) < 2017:
	print ("Barack Obama was US President")
if int(date) == 2017:
	print ("Barack Obama was US president or Donald J. Trump is US President")





