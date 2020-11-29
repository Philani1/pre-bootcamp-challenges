def test_number_65(num1, num2):
    sum = int(num1) + int(num2)     
    return num1 == 65 or num2 == 65 or sum == 65        

num1 = int(1)
num2 = int(64)

print(test_number_65(num1, num2))