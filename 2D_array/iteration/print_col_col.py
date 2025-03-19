# Print col-col

mat = [[1,1,1],[2,2,2],[3,3,3]]
M = 3
N = 3

for col in range(M):
  for row in range(N):
    print(mat[row][col], end = ' ')
  print()
