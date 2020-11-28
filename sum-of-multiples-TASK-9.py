
def sum_of_multiples():
    count = 1
    sum = 0
    for i in range(1, 1000):
        if count % 3 == 0:
            sum += count
        if count % 5 == 0:
            sum += count
        count += 1
    return sum

som = sum_of_multiples() 
print(f"The sum of all the multiples of 3 or 5 below 1000 is: {som}")
