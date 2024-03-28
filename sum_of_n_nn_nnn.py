'''
Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
Sample value of n is 5
Expected Result : 615
'''

def main():
    n = input("n: ")
    first = int(n)
    second = int(n + n)
    third = int(n + n + n)
    print(first + second + third)


if __name__ == "__main__":
    main()
