elements = int(input("Enter the number of elements in the array: "))
arr = []

i = 0
while i < elements:
    num = int(input(f"Enter elements {i+1}: "))
    arr.append(num)
    i = i+1

print("The elements in the array are: \n")
i = 0
while i < elements:
    print(arr[i])
    i = i + 1