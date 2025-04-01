#  Sum of Evens - Using while loop

A = int(input("Enter a positive integer: "))

cnt = 2
sum = 0
if cnt <= A:
  print(f"Even numbers in the range of 1 and {A}:")
while cnt <= A:
  print(cnt, end = " ")
  sum += cnt
  cnt += 2

print(f"\nSum of all evens: {sum}")



#  Sum of Evens - Using for loop
'''
A = int(input("Enter a positive integer: "))
sum = 0
if A >= 2:
  print(f"Even numbers in the range of 1 and {A}")
for i in range(2, A+1, 2):
  print(i, end = " ")
  sum += i

print(f"\nSum of all evens: {sum}")  
'''
