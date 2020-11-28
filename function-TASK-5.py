def area(a, b, c):
    semi_perimetre = (1/2)*(a+b+c)
    area = (semi_perimetre*(semi_perimetre-a)*(semi_perimetre-b)*(semi_perimetre-c))**(1/2)
    return area

Area = area(3, 4, 5)
print(f"Area of a triangle is: {Area} cm squared")