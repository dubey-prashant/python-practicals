# a.	Write a python program to convert Celsius to Fahrenheit.

def celsiusToFahrenheit(c):
    return (c * 9/5) + 32

userInput = int(input("Enter temperature in Celsius: "))

print(celsiusToFahrenheit(userInput))
