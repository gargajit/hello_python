''' Write a Python program to find the least common multiple (LCM) of two positive integers.'''

print("Using HCF")

def main():
    print("Enter two positive integers:")
    n1 = int(input("Number 1: "))
    n2 = int(input("Number 2: "))
    print("LCM:", find_lcm(n1, n2))


def find_lcm(n1, n2):
    if n1 == n2:
        return n1
    hcf = find_hcf(n1, n2)
    return int((n1 * n2) / hcf)


def find_hcf(n1, n2):
    dividend = 0
    divisor = 0
    remainder = 0
    hcf = 0

    if n1 > n2:
        dividend = n1
        divisor = n2
    elif n2 > n1:
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
