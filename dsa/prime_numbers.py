# Print Prime Numbers

ls = [1, 10, 7, 23, 2, 25, 27, 31]

n = len(ls)


primes = []

for i in range(n):
  is_prime = True
  if ls[i] < 2:
    is_prime = False

  f = 2
  while f * f <= ls[i]:
    if ls[i] % f == 0:
      is_prime = False
      break
    f += 1
      
      

  if is_prime:
    primes.append(ls[i])

print(primes)

