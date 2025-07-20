# Reverse an array using recursion

def rev_array(A, i, j):
  if i >= j:
    return
  
  A[i], A[j] = A[j], A[i]
  
  rev_array(A, i+1, j-1)


def main():
  arr = [10, 20, 30, 40, 50]
  start = 0
  end = len(arr) - 1
  

  rev_array(arr, start, end)
  print(arr)

if __name__ == "__main__":
  main()
