#  Reverse a Number - while
# You are given a number A. Your task is to reverse its digits of A and return the resulting number.

A = int(input())
reversed = 0

while A != 0:
  digit = A % 10
  reversed = reversed * 10 + digit
  A = A // 10

print(reversed)
