# Calculate Simple Interest

def simple_interest(p, r, t):
  return p * r * t / 100

principal = int(input("Enter the principal amount: "))
rate = int(input("Enter the rate of interest: "))
time = int(input("Enter the time in years: "))

simple_interest(principal, rate, time)
