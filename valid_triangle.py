# Angles Of Valid Triangle?

A, B, C = map(int, input("Enter the 3 angles (in degrees): ").split())

if A + B + C == 180 and A != 0 and B!= 0 and C != 0:
  if A == B == C :
    print("Equilateral Triangle")
  elif A != B and B != C and C != A:
    print("Scalene Triangle")
  else:
    print("Isosceles Triangle")

else:
  print("Not a valid Triangle!")
