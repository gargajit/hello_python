# One way
'''
while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an integer")
    else:
        break

print(f"x is {x}")
'''

# Second Way - No need for else
'''
while True:
    try:
        x = int(input("What's x? "))
        break
    except ValueError:
        print("x is not an integer")

print(f"x is {x}")
'''

# Third way

# Creating a get_int() function
'''
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            #print("x is not an integer")
            pass #**

main()

# ** If we do not want to prompt the exception but continue the loop
# i.e. instead of throwing message that x is not an integer we want to ask what's x
'''


# Fourth Way

# Let's refine the same program where the called function doesn't specify on it's own
# rather would take the prompt from the main itself

def main():
    x = get_int("What's x? ")       # now main has the prompt of What's x
    print(f"x is {x}")

def get_int(prompt):                # take prompt itself as the argument
    while True:
        try:
            return int(input(prompt))   #this will print the prompt asked in main
        except ValueError:
            pass

main()
