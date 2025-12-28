#1
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def subtract_fractions(A, B, C, D):
    num = A * D - C * B
    den = B * D
    g = gcd(abs(num), den)
    return num // g, den // g

A = int(input("Enter A: "))
B = int(input("Enter B: "))
C = int(input("Enter C: "))
D = int(input("Enter D: "))

num, den = subtract_fractions(A, B, C, D)
print(f"Result: {num}/{den}")


#2
n = int(input("Enter a number: "))

for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")























