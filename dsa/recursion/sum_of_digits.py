#  Problem 3: Sum of digits

def sum_of_digits(N):
  if N == 0:
    return 0
  
  digit = N % 10
  N = N // 10

  digit += sum_of_digits(N)
  return digit

def main():
  print(sum_of_digits(1000))

if __name__ == "__main__":
  main()
