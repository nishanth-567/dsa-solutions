elements = int(input("Enter the number of elements: "))
arr = []

i = 0
while i < elements:
    num = int(input(f"Enter number {i+1}: "))
    arr.append(num)
    i = i + 1

print("The array elements are:")
i = 0
while i < elements:
    print(arr[i])
    i = i + 1

