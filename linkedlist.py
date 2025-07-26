class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def delete(self, value):
        temp = self.head
        prev = None
        while temp:
            if temp.data == value:
                if prev:
                    prev.next = temp.next
                else:
                    self.head = temp.next
                return True
            prev = temp
            temp = temp.next
        return False

    def traverse(self):
        elements = []
        temp = self.head
        while temp:
            elements.append(temp.data)
            temp = temp.next
        return elements

    def search(self, value):
        temp = self.head
        pos = 0
        while temp:
            if temp.data == value:
                return pos
            temp = temp.next
            pos += 1
        return -1  # if not found

    def sort(self):
        # Bubble sort for linked list
        end = None
        while end != self.head:
            p = self.head
            while p.next != end:
                q = p.next
                if p.data > q.data:
                    p.data, q.data = q.data, p.data
                p = p.next
            end = p

# Example usage:
if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.insert(3)
    sll.insert(1)
    sll.insert(4)
    sll.insert(2)
    print("Traverse:", sll.traverse())
    print("Search 4:", sll.search(4))
    print("Delete 1:", sll.delete(1))
    print("Traverse after deletion:", sll.traverse())
    sll.sort()
    print("Traverse after sort:", sll.traverse())