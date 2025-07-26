# class Node:
#     def __init__(self, new_data):
#         #initialize
#         self.data = new_data
#         #next pointer to none
#         self.next = None
#
# def insert_at_front(head, new_data):
#     #new node with given data
#     new_node = Node(new_data)
#
#     #next of the new node point to the current head
#     new_node.next = head
#
#     #retrun new node as the current head
#     return new_node

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # Insert before a given element
    def insert_before(self, target, data):
        if not self.head:
            print("List is empty.")
            return
        if self.head.data == target:
            self.insert_at_beginning(data)
            return
        prev = None
        curr = self.head
        while curr and curr.data != target:
            prev = curr
            curr = curr.next
        if curr is None:
            print(f"Element {target} not found.")
            return
        new_node = Node(data)
        prev.next = new_node
        new_node.next = curr

    # Insert after a given element
    def insert_after(self, target, data):
        curr = self.head
        while curr and curr.data != target:
            curr = curr.next
        if curr is None:
            print(f"Element {target} not found.")
            return
        new_node = Node(data)
        new_node.next = curr.next
        curr.next = new_node

    # Delete at the beginning
    def delete_at_beginning(self):
        if not self.head:
            print("List is empty.")
            return
        temp = self.head
        self.head = self.head.next
        del temp

    # Delete at the end
    def delete_at_end(self):
        if not self.head:
            print("List is empty.")
            return
        if not self.head.next:
            temp = self.head
            self.head = None
            del temp
            return
        prev = None
        curr = self.head
        while curr.next:
            prev = curr
            curr = curr.next
        prev.next = None
        del curr

    # Delete at a particular nod
    def delete_node(self, value):
        if not self.head:
            print("List is empty.")
            return
        if self.head.data == value:
            self.delete_at_beginning()
            return
        prev = None
        curr = self.head
        while curr and curr.data != value:
            prev = curr
            curr = curr.next
        if not curr:
            print(f"Element {value} not found.")
            return
        prev.next = curr.next
        del curr

    #Delete after a given element
    def delete_after(self, target):
        curr = self.head
        while curr and curr.data != target:
            curr = curr.next
        if not curr or not curr.next:
            print(f"No element after {target} to delete.")
            return
        temp = curr.next
        curr.next = temp.next
        del temp

    #Sort the LL
    def sort(self):
        if not self.head or not self.head.next:
            return
        # Convert to list, sort, reconstruct linked list
        lst = []
        curr = self.head
        while curr:
            lst.append(curr.data)
            curr = curr.next
        lst.sort()
        self.head = None
        for data in reversed(lst):
            self.insert_at_beginning(data)


    # Delete entire list
    def delete_entire_list(self):
        curr = self.head
        while curr:
            temp = curr
            curr = curr.next
            del temp
        self.head = None

    # Utility to print the list
    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")

# Example usage
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_beginning(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    ll.insert_before(20, 15)
    ll.insert_after(30, 35)
    print("List after insertions:")
    ll.print_list()

    ll.delete_at_beginning()
    print("After deleting at beginning:")
    ll.print_list()

    ll.delete_at_end()
    print("After deleting at end:")
    ll.print_list()

    ll.delete_node(15)
    print("After deleting node 15:")
    ll.print_list()

    ll.delete_after(20)
    print("After deleting after 20:")
    ll.print_list()

    ll.insert_at_end(5)
    ll.insert_at_end(25)
    ll.sort()
    print("After sorting:")
    ll.print_list()

    ll.delete_entire_list()
    print("After deleting entire list:")
    ll.print_list()
