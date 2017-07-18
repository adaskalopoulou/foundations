# everytime we want to use a url

$ import requests

# some code that creates a new function
$ def display_image(url)

# to see the data
url = ...
response = requests.get(url)
data = response.json()

# to
type(data)

# 
data[][][]dictionary

#
len() list

for artist in artists:
  print(artist['name'])
  for image in artist['image']:
    if image['size'] == 'extralarge':
      print(image)
    print("----")

# to avoid gaps in urls instead of using comma use a +
# so instead of .replace we can do:

for mbid in mbids:
  print("htt;mn,sdadfja;dfkj" + mbid + "kajdfahdfajson")


numbers[:2]
#gives us the first two things of a list

for mbid in mbids[:3]:
  url = "..."
  print..url

for tag in tags:
  if tag['name'] == 'Hip-Hop' or tag['name'] == 'rap':
    print("they are a rapper")
  else:
    print("They are not a rapper")

# by default they are NOT a raper:
is_rapper = False
for tag in tags:
  if tag['name'] == 'Hip-Hop' or tag['name'] == 'rap':
    print("Found", tag['name'], "they are a rapper")
    is_rapper = True
  if is_rapper:
    print("Is a rapper")
else:
  print("Is not a rapper")











