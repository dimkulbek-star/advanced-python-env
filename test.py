def swap_first_last(arr):
    arr[0], arr[-1] = arr[-1], arr[0]

m = int(input("Enter array length: "))
A = []

for i in range(m):
    A.append(int(input()))

print("Original array:", A)

swap_first_last(A)

print("Modified array:", A)






