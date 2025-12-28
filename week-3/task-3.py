#1
import math

def hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

a1 = float(input("First leg of triangle 1: "))
b1 = float(input("Second leg of triangle 1: "))

a2 = float(input("First leg of triangle 2: "))
b2 = float(input("Second leg of triangle 2: "))

h1 = hypotenuse(a1, b1)
h2 = hypotenuse(a2, b2)

print("Hypotenuse of triangle 1:", h1)
print("Hypotenuse of triangle 2:", h2)

if h1 > h2:
    print("Triangle 1 has the greater hypotenuse")
elif h1 < h2:
    print("Triangle 2 has the greater hypotenuse")
else:
    print("Both hypotenuses are equal")





#2
text = input("Enter a string: ")

words = text.split()
sorted_words = []

for word in words:
    sorted_word = ''.join(sorted(word))
    sorted_words.append(sorted_word)

result = ' '.join(sorted_words)
print(result)













