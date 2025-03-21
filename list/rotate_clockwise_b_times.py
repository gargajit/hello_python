# Given a list of integers A as input and an integer B
# Rotate the list clockwise B times

A = [1, 2, 3, 4, 5]
B = 3

# [5, 1, 2, 3, 4]
# [4, 5, 1, 2, 3]
# [3, 4, 5, 1, 2]

# Note -> B will be less than length of A

# Approach 1 -> Using loops
# A = [1, 2, 3, 4, 5]
# B = 3
# for b in range(B) :
#   last = A.pop()
#   A.insert(0, last)
# print(A)

# Approach 2 -> Using slicing

# X = [1, 2]
# Y = [3, 4, 5]
# A = [X][Y]
# B = [Y][X]

X = A[ :-B]
Y = A[-B: ]
print(Y + X)
