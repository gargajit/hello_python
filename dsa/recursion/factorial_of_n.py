#  Problem 2: Factorial of N

def factorials(N):
  if N == 0 or N== 1:
    return 1
  return N * factorials(N-1)


def main():
  print(factorials(3))

if __name__ == "__main__":
  main()
