#MULTIPLICATION

#Multiplying integers
x = int(input('Enter first integer: '))
y = int(input('Enter second integer: '))

print("Multiplication:", x * y)
print()

#---------------------------------------------------------
#ADDITION

#Adding float values and rounding

x = float(input("Enter first float number: "))
y = float(input("Enter second float number: "))

print("Addition:", x + y)
print()

print("Let's round off the float value")
z = round(x + y)

print("Addition with rounded value: ", z)
print()

#------------
x = float(input("Enter first no: "))
y = float(input("Enter second no: "))

z = round(x + y)

print(f"{z:,}")

#---------------------------------------------------------
#DIVISION

#First Way: round function with 2 decimal places
x = float(input("Enter first no: "))
y = float(input("Enter second no: "))

z = round(x / y, 2)

print("Division: ", z)


#Second Way: rounding without round function and inside Fstring

x = float(input("Enter first no: "))
y = float(input("Enter second no: "))

z = x / y

print(f"{z:.2f}")

#---------------------------------------------------------
#Square of a number

def main():
    x = int(input("What's the value of x: "))
    print(f"{x} squared is", square(x))

def square(num):
    return num*num

main()
