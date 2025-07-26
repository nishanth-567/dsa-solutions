elements = int(input("Enter the number of elements in the array: \n"))
arr = []

#1
for i in range(elements):
    inp = int(input(f"Enter the element {i+1}: "))
    arr.append(inp)
print("Elements in the array after traversing:")
print(arr)

#2
arr.insert(1, 7)
print("Elements in the array after inserting 7 at index 1:")
print(arr)

#3
del_arr = []
for i in range(len(arr)):
    if i != 1:
        del_arr.append(arr[i])
arr = del_arr
print("Elements in the array after deleting the element at index 1")
print(arr)

#4
arr[3] = 4
print("Elements in the array after updating the element at index 3 to 4:")
print(arr)

