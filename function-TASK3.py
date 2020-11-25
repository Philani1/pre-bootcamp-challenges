def logic_funct(num1, num2):
    sum = num1 + num2     
    return num1 == 65 or num2 == 65 or sum == 65        

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print(logic_funct(num1, num2))