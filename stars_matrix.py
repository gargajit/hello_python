# Print a matrix of stars
# Given two integers N and M as inputs, print a rectangle of N * M stars.

N = int(input("N: "))
M = int(input("M: "))

print("\nUsing two loops:\n")
for n in range(1, N+1):
  for m in range(1, M+1):
    print("*", end = "")
  print()

print("\nUsing one loop:\n")
for n in range(1, N+1):
  print(M * "*")
