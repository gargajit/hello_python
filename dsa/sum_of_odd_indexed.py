# Sum of Odd indexed elements in a range

A = [2, 8, 3, 9, 15]
B = [ [1, 4],
      [0, 2],
      [2, 3] ]

def main():
  #arr = [3, 6, 2, 4, 3, 1, 9, 5, 7]
  arr = [2, 8, 3, 9, 15]
  #B = [[1,5],[2,7],[5,6]]
  B = [ [1, 4],
      [0, 2],
      [2, 3] ]
  print(sum_of_odd_idx_elements(arr, B))


def sumOfOddIndexedElements(A,B):
  N = len(A)
  Ps = [0] * N
  Q = len(B)
  res = [0] * Q

  for i in range(1, N):
    if i % 2 == 1:
      Ps[i] = Ps[i-1] + A[i]
    else:
      Ps[i] = Ps[i-1]

  for i in range(Q):
    L = B[i][0]
    R = B[i][1]

    if L > 0:
      res[i] = Ps[R] - Ps[L-1]
    else:
      res[i] = Ps[R]

  return res


if __name__ == "__main__":
  main()
