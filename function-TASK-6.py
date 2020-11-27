numbers = []

len_num = int(input("How many numbers do you to enter: "))

for i in range(len_num):
    numbers = numbers + [int(input("Enter number: "))]

def max_funct(number_list):
    max_no = 0
    for i in range(len(number_list)):
        num = number_list[i]
        if max_no == 0:
            max_no = num
        elif num > max_no:
            max_no = num
    return max_no

n_max = max_funct(numbers)
print(f"Maximum value is: {n_max}")
