def sum_of_multiples():
    sum = 0
    for count in range(0, 1000):
        if count % 3 == 0 or count % 5 == 0:
            sum += count
    return sum

if __name__ == "__main__":
    print(f"The sum of all the multiples of 3 or 5 below 1000 is: {sum_of_multiples()}")
