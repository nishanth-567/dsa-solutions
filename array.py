arr = []

n = int(input("Enter number of elements to insert: "))
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    arr.append(element)

print("Array after insertion:", arr)

# Delete
delete = int(input("Enter the value to delete: "))
if delete in arr:
    arr.remove(delete)
    print(f"{delete} deleted.")
else:
    print(f"{delete} not found in array.")

print("Array after deletion:", arr)

# Traverse
print("Traversing array elements:")
for item in arr:
    print(item, end=' ')
print()

# Size
print("Size of the array:", len(arr))
# Update
index = int(input("Enter the index to update: "))
if 0 <= index < len(arr):
    new_val = int(input("Enter new value: "))
    arr[index] = new_val
    print("Array after update:", arr)
else:
    print("Invalid index.")
