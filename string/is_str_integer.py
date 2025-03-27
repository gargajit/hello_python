S = input("Enter a string: ")

if S.isdigit():
  print(True)

elif len(S) != 0 and S[0] == "-" and S[1:].isdigit():
  print(True)

else:
  print(False)
