def logic_funct(num1, num2):
    sum = num1 + num2     
    return (num1 == 3 or num2 == 3) and sum % 10 == 3        

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print(logic_funct(num1, num2))