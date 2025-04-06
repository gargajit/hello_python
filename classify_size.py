# return the correct size

l = [15, 25, 35]

def classify_size(size):
  if 10 <= size <= 19:
    return "small"
  elif 20 <= size <= 29:
    return "medium"
  elif 30 <= size <= 39:
    return "large"
  
ans = [classify_size(size) for size in l]
print(ans)
