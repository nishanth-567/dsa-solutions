n = int(input("Enter the length of the array: "))

arr = []

for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    arr.append(element)

sum = sum(arr)
print("The elements of the array are []")
print(arr)
print("THe sum of the elements in the array is: ", sum)
