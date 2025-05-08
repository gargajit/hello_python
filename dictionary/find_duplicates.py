# Find duplicates
# Print all characters present >=2 times in the string
'''
sentence = "malaysia truly asia"

fm = {}

for s in sentence:
  if s not in fm:
    fm[s] = 1
  else:
    fm[s] += 1
    

for key in fm:
  if fm[key] >= 2:
    print(key, end = " ")
'''

# Cleaner Code

sentence = "malaysia truly asia"

fm = {}

for s in sentence:
  if s == " ":
        continue
  if s not in fm:
    fm[s] = 1
  else:
    fm[s] += 1

  if fm[s] == 2:
    print(s, end = " ")
