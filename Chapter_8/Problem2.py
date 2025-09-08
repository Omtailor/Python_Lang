# Write Python program to convert Celsius to Fahrenheit

def convert(celsius):
    fahrenheit = (celsius*9/5) + 32
    return fahrenheit

celsius = int(input("Enter Temperature: "))
x = convert(celsius)
print(f"{celsius} Degree Celsius is equal to {x} Degree Fahrenheit")