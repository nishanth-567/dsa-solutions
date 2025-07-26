# Python Program to Implement Array-Based Queue and Circular Queue

# First, implement a simple Linear Queue using a list.
# This supports enqueue (insert at end), dequeue (remove from front),
# insert_front (insert at beginning), and insert_end (same as enqueue).
# Note: Using list for queue is fine but dequeue/insert_front are O(n) operations.

class LinearQueue:
    def __init__(self):
        self.queue = []  # Initialize an empty list

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)  # Insert at end (O(1))

    def dequeue(self):
        if self.is_empty():
            return None  # Queue is empty
        return self.queue.pop(0)  # Remove from front (O(n))

    def insert_front(self, item):
        self.queue.insert(0, item)  # Insert at front (O(n))

    def insert_end(self, item):
        self.enqueue(item)  # Same as enqueue, insert at end

    def display(self):
        return self.queue  # Return the list for display


# Now, implement a Circular Queue using a fixed-size list (array).
# This uses modulo operation for wrapping around.
# We'll assume a fixed capacity to demonstrate circular behavior.

class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity  # Maximum size of queue
        self.queue = [None] * capacity  # Fixed-size list
        self.front = -1  # Front pointer
        self.rear = -1   # Rear pointer
        self.size = 0    # Current number of elements

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full! Cannot enqueue.")
            return
        if self.is_empty():
            self.front = 0  # First element
        self.rear = (self.rear + 1) % self.capacity  # Move rear circularly
        self.queue[self.rear] = item
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            return None  # Queue is empty
        item = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity  # Move front circularly
        self.size -= 1
        if self.is_empty():
            self.front = self.rear = -1  # Reset if empty
        return item

    def display(self):
        if self.is_empty():
            return []
        result = []
        i = self.front
        while True:
            result.append(self.queue[i])
            if i == self.rear:
                break
            i = (i + 1) % self.capacity
        return result


# Test Cases for Circular Queue
# Assume capacity=5 to demonstrate circular behavior (can wrap around)

print("Testing Circular Queue:")
cq = CircularQueue(5)  # Create circular queue with capacity 5

# Enqueue 10, 20, 30
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
print("After enqueue 10,20,30:", cq.display())  # Expected: [10, 20, 30]

# Dequeue twice: should get 10 and then 20
deq1 = cq.dequeue()
deq2 = cq.dequeue()
print("Dequeued items:", deq1, deq2)  # Expected: 10 20
print("After two dequeues:", cq.display())  # Expected: [30]

# Enqueue 5 (should add to the end, circularly if needed)
cq.enqueue(5)
print("After enqueue 5:", cq.display())  # Expected: [30, 5]

# To demonstrate circular wrap-around (optional, for understanding):
# Enqueue more items to fill and wrap
cq.enqueue(40)
cq.enqueue(50)
cq.enqueue(60)  # Now full: positions wrapped if needed
print("After enqueue 40,50,60:", cq.display())  # Expected: [30, 5, 40, 50, 60]
# Try enqueue when full
cq.enqueue(70)  # Should print "Queue is full!"

# Dequeue to show wrap-around
print("Dequeue after full:", cq.dequeue())  # 30
print("Queue now:", cq.display())  # [5, 40, 50, 60]


# Optional: Test Linear Queue
print("\nTesting Linear Queue:")
lq = LinearQueue()

# Enqueue (insert end)
lq.enqueue(10)
lq.enqueue(20)
lq.enqueue(30)
print("After enqueue 10,20,30:", lq.display())  # [10, 20, 30]

# Insert at front
lq.insert_front(5)
print("After insert_front 5:", lq.display())  # [5, 10, 20, 30]

# Insert at end (same as enqueue)
lq.insert_end(40)
print("After insert_end 40:", lq.display())  # [5, 10, 20, 30, 40]

# Dequeue
print("Dequeue:", lq.dequeue())  # 5
print("After dequeue:", lq.display())  # [10, 20, 30, 40]
