# Minimum Swaps

# Given an array of integers A and an integer B,
# find and return the minimum number of swaps required to bring
# all the numbers less than or equal to B together.

# Note: It is possible to swap any two elements, not necessarily consecutive.


def main():
  A = [1, 12, 10, 3, 14, 10, 5]
  B = 8
  print("Minimum swaps of all numbers less than B:", minSwaps(A,B))

def minSwaps(A,B):
  N = len(A)



if __name__ == "__main__":
  main()
