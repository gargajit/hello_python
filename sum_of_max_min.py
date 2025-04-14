# Given an array A of size N. You need to find the sum of Maximum and Minimum element in the given array.

def main():
  A = [-2, 1, -4, 5, 3]
  max_min(A)

def max_min(A):
  N = len(A)

  max = A[0]
  min = A[0]
  
  for i in range(1, len(A)):
      if A[i] > max:
          max = A[i]
      if A[i] < min:
          min = A[i]
      
  return (max + min)


if __name__ == "__main__":
  main()
