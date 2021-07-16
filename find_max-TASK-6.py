def find_max(num1, num2, num3):
    numbers_list = [num1, num2, num3]
    max_no = num1
    for i in range(len(numbers_list)):
        num = numbers_list[i]
        if num > max_no:
            max_no = num
    return max_no


if __name__ == "__main__":
    maximum_number = find_max(3, 4, 5)
    print(f"Maximum value is: {maximum_number}")
