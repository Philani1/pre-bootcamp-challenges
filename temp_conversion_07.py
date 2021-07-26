def celsius_to_fahrenheit(temp_celsius):
    cel_to_fahrenheit = (temp_celsius * 1.8) + 32
    return cel_to_fahrenheit


def fahrenheit_to_celsius(temp_fahrenheit):
    fahren_to_celsius = (temp_fahrenheit - 32) / 1.8
    return fahren_to_celsius


if __name__ == "__main__":
    print(
        f"The temperature {30} in celsius is: {celsius_to_fahrenheit(30)} in Fahrenheit \
        \nThe temperature {86} in fahrenheit is: {fahrenheit_to_celsius(86)} in Celsius"
    )
