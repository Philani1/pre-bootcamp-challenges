def logic_funct(num1, num2):
    sum = num1 + num2     
    return (num1 == 3 or num2 == 3) and sum % 10 == 3        

num1 = int(10)
num2 = int(3)

print(logic_funct(num1, num2))