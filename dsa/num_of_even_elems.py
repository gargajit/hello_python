# Number of even elements from l to r

def main():
  ar = [3,6,2,4,3,1,9,5,7]
  B = [[1,5],[2,7],[5,6]]
  print(evenNumberRange(ar, B))

def evenNumberRange(A, B):
  N = len(A)
  Q = len(B)
  Ps = [0] * N
  res = [0] * Q

  if A[0] % 2 == 0:
    Ps[0] = 1
  else:
    Ps[0] = 0

  for i in range(1,N):
    if A[i] % 2 == 0:
      Ps[i] = Ps[i-1] + 1
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
