S = "ABC"
new_S = ""

if 65 <= ord(S[0]) <= 90:
  for s in S:
    ascii_of_s = ord(s)
    add_32 = ascii_of_s + 32
    new_S += chr(add_32)

if 97 <= ord(S[0]) <= 122:
  for s in S:
    ascii_of_s = ord(s)
    sub_32 = ascii_of_s - 32
    new_S += chr(sub_32)

print(new_S)
