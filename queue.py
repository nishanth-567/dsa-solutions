class LinearQueue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def insert_front(self, item):
        self.queue.insert(0, item)

    def insert_end(self, item):
        self.enqueue(item)

    def display(self):
        return self.queue



class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full! Cannot enqueue.")
            return
        if self.is_empty():
            self.front = 0
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            return None
        item = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        if self.is_empty():
            self.front = self.rear = -1
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



print("Testing Circular Queue:")
cq = CircularQueue(5)

# Enqueue 10, 20, 30
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
print("After enqueue 10,20,30:", cq.display())

deq1 = cq.dequeue()
deq2 = cq.dequeue()
print("Dequeued items:", deq1, deq2)
print("After two dequeues:", cq.display())

cq.enqueue(5)
print("After enqueue 5:", cq.display())  # Expected: [30, 5]

cq.enqueue(40)
cq.enqueue(50)
cq.enqueue(60)
print("After enqueue 40,50,60:", cq.display())
cq.enqueue(70)

# Dequeue to show wrap-around
print("Dequeue after full:", cq.dequeue())
print("Queue now:", cq.display())


# Optional: Test Linear Queue
print("\nTesting Linear Queue:")
lq = LinearQueue()

# Enqueue (insert end)
lq.enqueue(10)
lq.enqueue(20)
lq.enqueue(30)
print("After enqueue 10,20,30:", lq.display())

# Insert at front
lq.insert_front(5)
print("After insert_front 5:", lq.display())

# Insert at end (same as enqueue)
lq.insert_end(40)
print("After insert_end 40:", lq.display())

# Dequeue
print("Dequeue:", lq.dequeue())  # 5
print("After dequeue:", lq.display())
