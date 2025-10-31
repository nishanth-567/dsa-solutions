import time
import random

def insertion_sort(arr):
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr

user_input = input("Enter integers separated by space: ")
arr = list(map(int, user_input.split()))

choice = input("Do you want to generate 50 random integers instead? (y/n): ").lower()
if choice == 'y':
    arr = [random.randint(1, 100) for _ in range(50)]
    print("Generated random list of 50 integers.")

print("\nOriginal list:", arr)

start_time = time.time()
sorted_insertion = insertion_sort(arr)
insertion_time = time.time() - start_time

start_time = time.time()
sorted_merge = merge_sort(arr.copy())
merge_time = time.time() - start_time

print("\nSorted using Insertion Sort:", sorted_insertion)
print("Sorted using Merge Sort:", sorted_merge)

print("\nPerformance Comparison:")
print(f"Insertion Sort Time: {insertion_time:.6f} seconds")
print(f"Merge Sort Time:     {merge_time:.6f} seconds")
