# Given a list of integers as input
# Rotate it clockwise by 1 position

ls = [1, 2, 3, 4]
# ans = [4, 1, 2, 3]

last = ls.pop()
ls.insert(0, last)
print(ls)
