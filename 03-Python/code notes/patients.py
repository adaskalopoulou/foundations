for patient in patients:
  if patient['temperature'] > 102:
    if patient['infection'] == 'No':
      print(patient['name'], ", your diagnosis is heat stroke.")
    else:
      print(patient['name'], ", take an aspirin and call me in the morning.")

for patient in patients:
  if patient['temperature'] > 98.6:
    if patient['infection'] == 'Yes':
      print(patient['name'], ", your diagnosis is the flu.")
    else:
      print(patient['name'], ", take an aspirin and call me in the morning.")

for patient in patients:
  if patient['infection'] == 'Yes':
    if patient['temperature'] < 98.6:
      print(patient['name'], ", your diagnosis is the cold.")
    else:
      print(patient['name'], ", take an aspirin and call me in the morning.")

