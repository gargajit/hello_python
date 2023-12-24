#One way - Better and my way - I would prefer this

def main():
    x = int(input("What's x? "))
    check_even(x)

def check_even(num):
    print("Even") if num % 2 == 0 else print("Odd")

main()



#Comment other codeblocks
#Second Way - not so good
"""
def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
main()
"""
#Comment other codeblocks
#More Pythonic way to write the Second way
"""
def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(num):
    return True if num % 2 == 0 else False

main()
"""

#Most concise and pythonic way
"""
def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(num):
    return num % 2 == 0

main()
"""
