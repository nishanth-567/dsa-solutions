n = int(input("Enter the length of the array: "))

arr = []

for i in range(n):
    numbers = int(input("Enter the numbers: "))
    arr.append(numbers)

print("Maximum value is: ", max(arr))
print("Minimum value is: ", min(arr))