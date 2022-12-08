from math import pi


def area_of_circle():
    radius = float(input("Enter the radius of the circle: "))
    result = pi * radius * radius
    print("area of circle is: ", result)


area_of_circle()
