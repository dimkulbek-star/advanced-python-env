#1
import math
choice = int(input("Enter your choice (1.Circle 2.Rectangle 3.Triangle): "))
if choice == 1:
    r = float(input("Enter radius: "))
    area = math.pi * r * r
    print("Area of the circle:", area)
elif choice == 2:
    a = float(input("Enter length: "))
    b = float(input("Enter width: "))
    area = a * b
    print("Area of the rectangle:", area)
elif choice == 3:
    b = float(input("Enter base: "))
    h = float(input("Enter height: "))
    area = 0.5 * b * h
    print("Area of the triangle:", area)
else:
    print("Invalid choice")


#2
arrays = [
    [1, 2, 3, 4],
    [5, 10, 15],
    [7, 14, 21, 28]
]
for i in range(3):
    arr = arrays[i]
    total = sum(arr)
    mean = total / len(arr)
    print("Arithmetic mean = ", mean)
    print()





