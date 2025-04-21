# Find the sum of elements from index l to r with Prefix Sum


def main():
  A = [-5, 10, 20, 40, 50, -10, 80, -90, -20]
  B = [[1,3],[0,4],[6,8]]

  print(withPs(A, B))


def withPs(A, B):
  N = len(A)
  Q = len(B)
  Ps = [0]*N
  res = [0]*Q

  for i in range(1, N):
    Ps[i] = Ps[i-1] + A[i]

  for i in range(Q):
    l = B[i][0]
    r = B[i][1]
    
    if l > 0:
      res[i] = Ps[r] - Ps[l-1]
    else:
      res[i] = Ps[r]
  
  return res


if __name__ == "__main__":
  main()
