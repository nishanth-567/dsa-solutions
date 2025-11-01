class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete_front(self):
        if self.head is None:
            print("List is empty.")
        else:
            self.head = self.head.next

    def traverse(self):
        temp = self.head
        if not temp:
            print("List is empty.")
            return
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            print("Stack is empty.")
            return None
        popped = self.top.data
        self.top = self.top.next
        return popped

    def peek(self):
        if self.top is None:
            print("Stack is empty.")
            return None
        return self.top.data

    def is_empty(self):
        return self.top is None


print("Nishanth, 24217, CSE-C")
print("Linked List Operations:")
ll = LinkedList()
n = int(input("Enter number of elements to insert in linked list: "))
for i in range(n):
    val = int(input(f"Enter value {i+1}: "))
    ll.insert_end(val)

print("Linked list elements:")
ll.traverse()

choice = input("Do you want to insert at front? (y/n): ").lower()
if choice == 'y':
    val = int(input("Enter value to insert at front: "))
    ll.insert_front(val)

print("Linked list after insertion:")
ll.traverse()

choice = input("Do you want to delete from front? (y/n): ").lower()
if choice == 'y':
    ll.delete_front()

print("Linked list after deletion:")
ll.traverse()

print("\nStack Operations:")
stack = Stack()
n = int(input("Enter number of elements to push into stack: "))
for i in range(n):
    val = int(input(f"Enter value {i+1}: "))
    stack.push(val)

choice = input("Do you want to pop an element? (y/n): ").lower()
if choice == 'y':
    print("Popped element:", stack.pop())

print("Current top element (peek):", stack.peek())

