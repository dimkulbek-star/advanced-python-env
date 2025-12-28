#1

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

A = int(input("Enter A: "))
B = int(input("Enter B: "))

print("GCD:", gcd(A, B))
print("LCM:", lcm(A, B))


#2
import math

def triangle_area(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
d = float(input("Enter side d: "))
diag = float(input("Enter diagonal: "))

area = triangle_area(a, b, diag) + triangle_area(c, d, diag)
print("Area of the quadrilateral:", area)






























