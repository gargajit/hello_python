A = [[1,2],[3,4]]
B = [[9,10],[11,12]]

sum = []
for row in range(len(A)):
  ls = []
  for col in range(len(A[0])):
    ls.append(A[row][col] + B[row][col])
  sum.append(ls)
print(sum)    
