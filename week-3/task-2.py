#1

import math

def triangle_area(base, height):
    return 0.5 * base * height

def hexagon_area(a):
    height = (math.sqrt(3)/2) * a
    return 6 * triangle_area(a, height)

a = float(input("Enter the side of the hexagon: "))
print("Area of the hexagon:", hexagon_area(a))

#2
def rectangle_area(length, width):
    return length * width

for i in range(1, 4):
    print(f"Rectangle {i}:")
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    print(f"Area of rectangle {i}: {rectangle_area(length, width)}")




























