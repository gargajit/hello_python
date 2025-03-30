#  Search Element#
#  You are given an integer T (number of test cases). 
# You are given array A and an integer B for each test case. 
# You have to tell whether B is present in array A or not.

def main():
    T = int(input("Number of Test Cases: "))

    for t in range(1, T+1):
        N = int(input("Length of the list: "))
        A = list(map(int, input(f"Enter list values of length {N}: ").split()))
        B = int(input("Enter a number: "))

        if B in A:
          print(f"{B} is in the List")
        else:
          print(f"{B} is not in the List")

if __name__ == '__main__':
    main()
