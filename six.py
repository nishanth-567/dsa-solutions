import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        heapq.heappush(self.heap, value)

    def extract_min(self):
        if len(self.heap) == 0:
            print("Heap is empty.")
            return None
        return heapq.heappop(self.heap)

    def heapify(self):
        heapq.heapify(self.heap)

    def display(self):
        print("Current Heap:", self.heap)

    def heap_sort(self):
        sorted_list = []
        temp_heap = self.heap[:]
        while temp_heap:
            sorted_list.append(heapq.heappop(temp_heap))
        return sorted_list


min_heap = MinHeap()

n = int(input("Enter number of elements to insert in the heap: "))
for i in range(n):
    value = int(input(f"Enter element {i+1}: "))
    min_heap.insert(value)

min_heap.display()

choice = input("Do you want to extract min element? (y/n): ").lower()
if choice == 'y':
    print("Extracted Min:", min_heap.extract_min())
    min_heap.display()

print("Heap after heapify:")
min_heap.heapify()
min_heap.display()

print("Heap Sort Result (Ascending Order):", min_heap.heap_sort())
