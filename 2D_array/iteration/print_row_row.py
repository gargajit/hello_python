# Print row-row
mat = [[1,1,1],[2,2,2],[3,3,3]]
M = 3
N = 3

for row in range(N):
  for col in range(M):
    print(mat[row][col], end= ' ')
  print()
