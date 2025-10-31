class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.queue:
            print("Queue is empty.")
            return None
        return self.queue.pop(0)

    def front(self):
        if not self.queue:
            print("Queue is empty.")
            return None
        return self.queue[0]

    def display(self):
        print("Queue:", self.queue)


class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def enqueue(self, item):
        if (self.rear + 1) % self.size == self.front:
            print("Circular Queue is full.")
            return
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = item

    def dequeue(self):
        if self.front == -1:
            print("Circular Queue is empty.")
            return None
        removed = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return removed

    def display(self):
        if self.front == -1:
            print("Circular Queue is empty.")
            return
        print("Circular Queue:", end=" ")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()


print("Normal Queue Operations:")
q = Queue()
n = int(input("Enter number of elements to enqueue: "))
for i in range(n):
    val = int(input(f"Enter value {i+1}: "))
    q.enqueue(val)
q.display()

choice = input("Do you want to dequeue an element? (y/n): ").lower()
if choice == 'y':
    print("Dequeued element:", q.dequeue())
q.display()

if q.queue:
    print("Front element:", q.front())

print("\nCircular Queue Operations:")
size = int(input("Enter size of circular queue: "))
cq = CircularQueue(size)
n = int(input("Enter number of elements to enqueue initially: "))
for i in range(n):
    val = int(input(f"Enter value {i+1}: "))
    cq.enqueue(val)
cq.display()

choice = input("Do you want to dequeue an element? (y/n): ").lower()
if choice == 'y':
    print("Dequeued element:", cq.dequeue())
cq.display()

choice = input("Do you want to enqueue another element? (y/n): ").lower()
if choice == 'y':
    val = int(input("Enter value to enqueue: "))
    cq.enqueue(val)
cq.display()
