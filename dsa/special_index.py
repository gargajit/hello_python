# Special Index
# Given an array, arr[] of size N, the task is to find the count of array
# indices such that removing an element from these indices makes the sum
#  of even-indexed and odd-indexed array elements equal.

def main():
  ar = [4,3,2,7,6,-2]
  print(specialIndex(ar))

def specialIndex(A):
  N = len(A)
  Ps_odd = [0] * N
  Ps_even = [0] * N

  Ps_odd[0] = 0
  Ps_even[0] = A[0]

  # Odd indexed Prefix Sum
  for i in range(1,N):
    if i % 2 == 1:
      Ps_odd[i] = Ps_odd[i-1] + A[i]
    else:
      Ps_odd[i] = Ps_odd[i-1]

  # Even indexed Prefix Sum
  for i in range(1, N):
    if i % 2 == 0:
      Ps_even[i] = Ps_even[i-1] + A[i]
    else:
      Ps_even[i] = Ps_even[i-1]


  cnt = 0
  if ((Ps_even[N-1] - Ps_even[N-1]) == (Ps_odd[N-1] - Ps_odd[0])):
    cnt += 1

  for i in range(1, N):
    if ((Ps_odd[i-1] + Ps_even[N-1] - Ps_even[i]) == (Ps_even[i-1] + Ps_odd[N-1] - Ps_odd[i])):
      cnt += 1

  return cnt

if __name__ == "__main__":
  main()
