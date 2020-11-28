def celsius_to_fahrenheit(temp_celsius):
    fahrenheit = (temp_celsius * 1.8) + 32
    return fahrenheit

def  fahrenheit_to_celsius(temp_fahrenheit):
    celsius = (temp_fahrenheit - 32) / 1.8
    return celsius  


temp_celsius = float(30)
temp = celsius_to_fahrenheit(temp_celsius)
print(f"The temperature {temp_celsius} in celsius is: {temp} in Fahrenheit")

temp_fahrenheit = float(86)
temp = fahrenheit_to_celsius(temp_fahrenheit)
print(f"The temperature {temp_fahrenheit} in fahrenheit is: {temp} in Celsius")

