#main function
def main():
    name = input("Enter your name: ").strip().title()
    hello(name)

#hello function 
def hello(to='World'):
    print("Hello,", to + "!")

#calling main function
main()
