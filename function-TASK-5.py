a = float(input("Enter the first side length in cm: "))
b = float(input("Enter the second side length in cm: "))
c = float(input("Enter the last side length in cm: "))

def area(a, b, c):
    if(a == b and b == c):
        area = ((b*b) * (3**(1/2.0)/4))
    else:
        s = (1/2)*(a+b+c)
        area = (s*(s-a)*(s-b)*(s-c))**(1/2)
    return area

Area = area(a, b, c)
print(f"Area of a triangle is: {Area} cm squared")