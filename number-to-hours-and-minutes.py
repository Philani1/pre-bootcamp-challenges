num = int(input("Enter number: "))

def number_to_HM(num):
    hours = num/60
    minutes = num%60

    return f"{int(hours)} hours, {minutes} minutes"

print(number_to_HM(num))