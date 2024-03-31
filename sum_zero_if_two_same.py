'''Write a Python program to sum three given integers. However, if two values are equal, the sum will be zero'''

def main():
    x = int(input("1st number: "))
    y = int(input("2nd number: "))
    z = int(input("3rd number: "))

    sum = 0

    if x == y or y == z or x == z: 
        print(f"Sum = {sum}")

    else:
        sum = x + y + z
        print(f"Sum = {sum}")


if __name__ == "__main__":
    main()
