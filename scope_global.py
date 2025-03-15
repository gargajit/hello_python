# Scope where want to change the value of global inside function

a = 1

def fun():
  global a
  a = 2
  print(a)

fun()
print(a)
