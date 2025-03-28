n = int(input("n: "))

# Method 1

i = 2
while i <= 2*n:
  if i % 2 == 0:
    print(i, end = ' ')
  i += 1

# Method 2 - Better Time Complexity

for i in range(2, (n*2)+1, 2):
  print(i, end = ' ')
