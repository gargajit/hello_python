#  Problem 1: Print numbers from 1 to N using Recursion

def print_nums(N):
  if N == 0:
    return
  print_nums(N-1)
  print(N, end = " ")

def main():
  print_nums(10)

if __name__ == "__main__":
  main()
