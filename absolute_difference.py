'''
Write a Python program to calculate the difference between a given number and 17. 
If the number is greater than 17, return twice the absolute difference.
'''

def main():
    num = int(input("Enter num: "))
    print(abs_difference(num))


def abs_difference(n):
    if n > 17:
        return 2 * abs(n - 17)
    else:
        return abs(n - 17)
    
if __name__ == "__main__":
    main()
