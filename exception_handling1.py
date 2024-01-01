#One way
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

#Second Way - No need for else
'''
while True:
    try:
        x = int(input("What's x? "))
        break
    except ValueError:
        print("x is not an integer")

print(f"x is {x}")
'''

# Creating a get_int() function

def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("What's x? "))
            break
        except ValueError:
            print("x is not an integer")
    return x

main()
