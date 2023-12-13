dzn = 2
time = 5
price = 80
order = "I will take {} dozen bananas at {}pm for a price of {}rs."
print(order.format(dzn, time, price))

#Use index numbers to select the position of integer in the text
dzn = 2
person = "Ajit"
time = 5
price = 80
order = "At {2}pm, the price of {0} dozen bananas will be {3}rs. This is when {1} will take the order."
print(order.format(dzn, person, time, price))

"""Custom object instances can be passed to the format() function 
as long as it specifies the __str__ method."""
class Person:
    
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return self.name

dzn = 2
person = Person("Rithik")
time = 5
price = 80
order = "{} will take {} dozen bananas at {}pm for a price of {}rs."
print(order.format(person, dzn, time, price))
