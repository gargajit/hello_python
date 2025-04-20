# How many Prime Numbers are there?

def main():
  l = list(map(int, input("Enter the Numbers: ").split()))
  prime_nos = num_of_primes(l)
  print(f"In the given list of numbers, the number of prime numbers are: {prime_nos}")

def num_of_primes(ls):
  cnt = 0
  i = 0
  while i < len(ls):
    is_prime = True
    if ls[i] < 2:
      is_prime = False

    else:
       j = 2
       while j * j <= ls[i]:
        if ls[i] % j == 0:
          is_prime = False
          break
        j += 1

    if is_prime:
      cnt += 1

    i += 1

  return cnt

if __name__ == "__main__":
  main()

