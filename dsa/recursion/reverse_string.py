# Reverse a String (Recursively, but NO slicing allowed)

def reverse_string(s, i, j):
  ans_str = ""
  def helper(s, j):
    # nonlocal ans_str
    if j == 0:
      return s[j] 
    
    # ans_str = s[j] + helper(s, j-1)
    # return ans_str
    return s[j] + helper(s, j-1)

  return helper(s, j)

def main():
  s = "Hello"
  start = 0
  end = len(s) - 1

  print(reverse_string(s, start, end))

if __name__ == "__main__":
  main()
