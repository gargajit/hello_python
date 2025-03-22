# Given a list of integers, find its mode
# Mode -> Item which occurs most frequently

# Using count function

ls = [1,2,4,3,1,2,2,3]

mode = ls[0]

for item in ls:
  if ls.count(item) > ls.count(mode):
    mode = item

print(mode)
