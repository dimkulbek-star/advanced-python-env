#1
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def divide_fractions(A, B, C, D):
    num = A * D
    den = B * C
    g = gcd(num, den)
    return num // g, den // g

A = int(input("Enter A: "))
B = int(input("Enter B: "))
C = int(input("Enter C: "))
D = int(input("Enter D: "))

num, den = divide_fractions(A, B, C, D)
print(f"Result: {num}/{den}")

#2
def is_inside_circle(x, y, a, b, R):
    return (x - a)**2 + (y - b)**2 < R**2
a = float(input("Enter a (center x): "))
b = float(input("Enter b (center y): "))
R = float(input("Enter radius R: "))
points = [
    (float(input("p1: ")), float(input("p2: "))),
    (float(input("f1: ")), float(input("f2: "))),
    (float(input("l1: ")), float(input("l2: ")))
]
count = 0
for x, y in points:
    if is_inside_circle(x, y, a, b, R):
        count += 1
print("Number of points inside the circle:", count)




