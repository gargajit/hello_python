# 'A' to 'Z' → 65 to 90
# 'a' to 'z' → 97 to 122

char = input("Enter the first letter (case sensitive): ")
n = int(input(f"Enter the number of consecutive letters to be printed after {char}: "))

ascii_val_of_char = ord(char)

last_char_ascii_val = ascii_val_of_char + n

for i in range(ascii_val_of_char, last_char_ascii_val + 1):
  current_char = chr(i)
  print(current_char, end = ' ')
