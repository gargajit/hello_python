# Print a square of N * N stars
N = int(input())
for row in range (1, N+1):
  for i in range (1, N+1):
    print("*", end=' ')
  print()
