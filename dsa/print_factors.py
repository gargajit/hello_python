# print the factors

N = int(input("Enter a number: "))

i = 1
while i * i <= N:
  if N % i == 0:
    if i == N/i:
      print(int(i), end = ' ')
    else:
      print(int(i), int(N/i), end = " ")
  i += 1
