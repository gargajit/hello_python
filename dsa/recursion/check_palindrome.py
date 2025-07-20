# Check if a String is a Palindrome (Recursively)

def is_palindrome(s: str, i: int , j: int) -> bool:  

  if i >= j:
    return True
  
  if s[i] != s[j]:
    return False
  
  return is_palindrome(s, i+1, j-1)



def main():
  str_list = ["", 
              "a", 
              "apple", 
              "madam", 
              "racecar", 
              "A man a plan a canal Panama", 
              "Was it a car or a cat I saw", 
              "No lemon, no melon", 
              "Hello World"
              ]


  for s in str_list:
    st = "".join(s.split())
    st = st.lower()
    start = 0
    end = len(st) - 1


    if is_palindrome(st, start, end):
      print(f"'{s}' is palindrome. ✅")
    else:
      print(f"'{s}' is not palindrome. ❌")

if __name__ == "__main__":
  main()
