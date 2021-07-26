def calculate_area(side_a, side_b, side_c):
    semi_perimetre = (1 / 2) * (side_a + side_b + side_c)
    area = (
        semi_perimetre
        * (semi_perimetre - side_a)
        * (semi_perimetre - side_b)
        * (semi_perimetre - side_c)
    ) ** (1 / 2)

    return area


if __name__ == "__main__":
    print(calculate_area(3, 4, 5))
