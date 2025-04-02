# Celsius to Fahrenheit
# Round the output up to 2 decimal places
# The formula to convert Celsius to Fahrenheit is: F = (9/5 * C) + 32


temp_in_cel = float(input())

ans = (9/5 * temp_in_cel) + 32

print(f"Fahrenheit: {round(ans, 2)}")
