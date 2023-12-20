#Take Name Input
name = input("What's your name? ")
print("Hello,", name + "!")
print()

#Print Documentataion: print(*objects, sep=' ', end='\n', file=st.stdout, flush=False)

#Modifying end parameter
print("Bad:")
print("Hi,")
print(name)
print()
print("Good:")
print("Hi, ", end="")
print(name)
print()

#Modifying separator parameter
print("Bad:")
print("Hello, ", name + "!")
print()
print("Good:")
print("Hello, ", name + "!", sep="")



