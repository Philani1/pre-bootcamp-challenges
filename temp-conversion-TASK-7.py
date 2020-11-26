def celsius_to_fahrenheit(temp_celsius):
    fahrenheit = (temp_celsius * 1.8) + 32
    return fahrenheit

def  fahrenheit_to_celsius(temp_fahrenheit):
    celsius = (temp_fahrenheit - 32) / 1.8
    return celsius  

temp_celsius = float(input("Enter temperature in Celsius: "))
temp = celsius_to_fahrenheit(temp_celsius)
print(f"The temperature in Fahrenheit is: {temp}")

temp_fahrenheit = float(input("\nEnter temperature in Fahrenheit: "))
temp = fahrenheit_to_celsius(temp_fahrenheit)
print(f"The temperature in Celsius is: {temp}")
