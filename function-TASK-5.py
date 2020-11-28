def area(side_a, side_b, side_c):
    semi_perimetre = (1/2)*(side_a + side_b + side_c)
    area = (semi_perimetre * (semi_perimetre - side_a)*(semi_perimetre - side_b)*(semi_perimetre - side_c))**(1/2)
    return area

Area = area(3, 4, 5)
print(f"Area of a triangle is: {Area} cm squared")