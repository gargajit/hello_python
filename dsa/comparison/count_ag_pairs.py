import time

def bruteForce_countAGPairs(s):
  N = len(s)
  count = 0

  for i in range(N-1):
    if s[i] == 'a':
      for j in range(i+1, N):
        if s[j] == 'g':
          count += 1
  return count

def optimized_countAGPairs(s):
  N = len(s)
  count = 0
  num_of_a = 0

  for i in range(N):
    if s[i] == 'a':
      num_of_a += 1
    if s[i] == 'g':
      count += num_of_a

  return count


def main():
  s = 'a' * 5000 + 'g' * 5000

  start = time.time()
  brute_result = bruteForce_countAGPairs(s)
  brute_time = time.time() - start

  start = time.time()
  optimised_result = optimized_countAGPairs(s)
  optimised_time = time.time() - start


  print(f"Brute-force result: {brute_result}, Time: {brute_time:.4f}s")
  print(f"Optimized result:   {optimised_result}, Time: {optimised_time:.4f}s")


if __name__ == "__main__":
  main()
