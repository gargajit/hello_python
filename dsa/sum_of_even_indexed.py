# Sum of Even indexed elements in a range

def main():
  A = [-5, 10, 20, 40, 50, -10, 80, -90, -20]
  B = [[1,3],[0,4],[6,8]]
  
  print(evenRange(A,B))

def evenRange(A,B):
  N = len(A)
  Q = len(B)
  Ps = [0]*N
  Ps[0] = A[0]
  res = [0]*Q

  for i in range(1, N):
    if i % 2 == 0:
      Ps[i] = Ps[i-1] + A[i]
    else:
      Ps[i] = Ps[i-1]
  
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
