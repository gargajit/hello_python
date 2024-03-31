'''Write a Python program to sum three given integers. However, if two values are equal, the sum will be zero'''

def main():
    n1 = int(input("1st number: "))
    n2 = int(input("2nd number: "))
    n3 = int(input("3rd number: "))

    sum = 0

    if (n1 == n2 or n1 == n3) and n2 != n3:
        print(f"Sum = {sum}")

    elif (n2 == n1 or n2 == n3) and n1 != n3:
        print(f"Sum = {sum}")
        
    else:
        sum = n1 + n2 + n3
        print(f"Sum = {sum}")


if __name__ == "__main__":
    main()
