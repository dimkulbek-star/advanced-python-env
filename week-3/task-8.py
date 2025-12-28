#1
n = int(input("Enter n: "))

for num in range(1, n + 1):
    digits = str(num)
    valid = True

    for d in digits:
        if d == '0' or num % int(d) != 0:
            valid = False
            break

    if valid:
        print(num, end=" ")


#2
















