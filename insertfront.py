# class Node:
#     def __init__(self, new_data):
#         #initialize
#         self.data = new_data
#         #set next pointer to none
#         self.next = None
#
# def insert_at_front(head, new_data):
#     #create a new node with the given data
#     new_node = Node(new_data)
#     #make the next of the new node point to the current head
#     new_node.next = head
#     return new_node
#
# def print_list(head):
#     #startiing from the head of the list
#     curr = head
#     #traverse through the list
#     while curr is not None:
#         print(f"{curr.data}", end="")
#         #move to the next node
#         curr = curr.next
#         #print a new line
#         print()
#
# #Print the functions
# if __name__ == "__main__":
#     #creating a LL with 2,3,4,5
#     head = Node(2)
#     head.next = Node(3)
#     head.next.next = Node(4)
#     head.next.next.next = Node(5)
#
#     #prijt the original list
#     print("Original list: \n", end="")
#     print_list(head)
#
#     #Insert a new element at the front
#     print("Elements after insertin an element at the front: \n", end="")
#     data = 1
#     head = insert_at_front(head, data)
#
#     print_list(head)







# class Node:
#     def __init__(self, new_data):
#         #Initialize
#         self.data = new_data
#         #set the next to none
#         self.next = None
#
# def insert_at_front(head, new_data):
#     #create a new node with the given data
#     new_node = Node(new_data)
#     new_node.next = head
#     return new_node
#
# def print_list(head):
#     curr = head
#     while curr is not None:
#         print(f"{curr.data}", end="")
#         curr = curr.next
#         print()
#
#
# if __name__ == "__main__":
#     head = Node(2)
#     head.next = Node(3)
#     head.next.next = Node(4)
#     head.next.next.next = Node(5)
#
#     print("Original Linked List before inserting an element: \n", end="")
#     print_list(head)
#
#     print("Linked list after inserting an element at the front: \n", end="")
#     data = 1
#     head = insert_at_front(head, data)
#     print_list(head)


class Node:
    def __init__(self, new_data):
        #initialize
        self.data = new_data
        self.next = None

def insert_at_front(head, new_data):
    new_node = Node(new_data)
    new_node.next = head
    return new_node

def print_list(head):
    curr = head
    while curr is not None:
        print(f"{curr.data}", end="")
        curr = curr.next
        print()

if __name__ == "__main__":
    head = Node(2)
    head.next = Node(3)
    head.next.next = Node(4)
    head.next.next.next = Node(5)

    print("Original Linked List before inserting an element: \n", end="")
    print_list(head)

    print("Linked list after inserting an element at the front: \n", end="")
    data = 1
    head = insert_at_front(head, data)
    print_list(head)


