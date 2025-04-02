# Count the digits

# Take T (number of test cases) as input.
# For each test case, take integer N as input and 
# Print the count of digits of that number.

# Note: No of digits for number 0 is considered as 1.


T = int(input("Number of Test Cases: "))

for t in range(1, T+1):
  N = input("Enter a number: ")
  print(f"Number of digits: {len(N)}")
