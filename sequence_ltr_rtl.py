def sequence(n):
  for i in range(1, n+1):
        if i == n:
            print(i)
        else:
            print(i, end= ' ')
  for j in range(n, 0, -1):
        print(j, end = ' ')

def main():
  N = int(input())
  sequence(N)

if __name__ == "__main__":
  main()
