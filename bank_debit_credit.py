# You have been provided with a bank account that has an initial balance of N amount. 
# You are now required to perform two operations on this account, 
# namely, ADD and SUBTRACT.

N = int(input("Enter the initial balance: "))
M = int(input("Number of operations to be performed: "))

i = 1
while i <= M:
  type, amt = map(int, input("'1' to CREDIT, '2' to DEBIT followed by the amount: ").split())
  if type == 1:
    N += amt
    print("New Balance:", N)
  elif type == 2:
    if amt > N:
      print("Insufficient Balance")
    else:
      N -= amt
      print("New Balance:", N)
      
  i += 1
