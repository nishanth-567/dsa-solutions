def traverse_list(arr):
    for element in arr:
        print(element, end=" ")
    print()

def insert_element(arr, index, value):
    arr = arr[:index] + [value] + arr[index:]
    return arr

def delete_element(arr, index):
    arr = arr[:index] + arr[index+1:]
    return arr

def linear_search(arr, value):
    for i in range(len(arr)):
        if arr[i] == value:
            return i
    return -1

def update_element(arr, index, value):
    arr[index] = value
    return arr

arr = list(map(int, input("Enter elements of the list separated by space: ").split()))

print("Original list:")
traverse_list(arr)

index = int(input("Enter index to insert: "))
value = int(input("Enter value to insert: "))
arr = insert_element(arr, index, value)
print("After insertion:")
traverse_list(arr)

index = int(input("Enter index to delete: "))
arr = delete_element(arr, index)
print("After deletion:")
traverse_list(arr)

value = int(input("Enter element to search: "))
index = linear_search(arr, value)
if index != -1:
    print(f"Element found at index: {index}")
else:
    print("Element not found")

index = int(input("Enter index to update: "))
value = int(input("Enter new value: "))
arr = update_element(arr, index, value)
print("After update:")
traverse_list(arr)