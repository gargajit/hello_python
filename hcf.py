'''Write a Python program that computes the greatest common divisor/ highest common factor (HCF) of two positive integers.'''

print('''
      Using Euclid's Algorithm:
      Step 1: Divide the larger number by the smaller number.
      Step 2: Replace the larger number with the remainder.
      Step 3: Repeat until the remainder is 0. The divisor at this point is the GCD.
      ''')

def main():
    print("Enter two positive integers:")
    n1 = int(input("Number 1: "))
    n2 = int(input("Number 2: "))
    print("HCF:", find_hcf(n1, n2))

def find_hcf(n1, n2):
    dividend = 0
    divisor = 0
    remainder = 0
    hcf = 0

    if n1 > n2:
        dividend = n1
        divisor = n2
    else:
        dividend = n2
        divisor = n1
    
    while True:
        remainder = dividend % divisor
        if remainder != 0:
            dividend = divisor
            divisor = remainder
        else:
            hcf = divisor
            break

    return hcf

if __name__ == "__main__":
    main()
