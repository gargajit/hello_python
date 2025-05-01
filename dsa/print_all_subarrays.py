# Print all possible subarrays of the array

A = [3,4,9]
N = len(A)
for i in range(N):      # start index
  for j in range(i, N): # end index
    for k in range(i, j+1):
      print(A[k], end = " ")

    print()
