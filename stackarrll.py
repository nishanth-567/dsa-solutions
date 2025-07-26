#Implement stacks using arrays and LL

class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

#class to implement stack using single LL
class Stack:
    def __init__(self):
        # head of the linked list
        self.head = None

    #function for 'is empty'
    def is_empty(self):
        # if head is empty, then head is none
        return self.head is None

    #push an element into the stack
    def push(self, new_data):
        # create a new node
        new_node = Node(new_data)

        #check if memory allocation for the new node failed
        if not new_node:
            print("\nStack Overflow")
            return

        #link the new node to the current top node
        new_node.next = self.head

        # update it to the new node
        self.head = new_node

    #function to remove the top element
    def pop(self):
        #check for stack underfloq
        if self.is_empty():
            print("\nStack Underflow")
        else:
            #assign the current top variable to temp value
            temp = self.head
            self.head = self.head.next
            del temp

    #funtion to return to the top elemet of the stack
    def peek(self):
        # if stack is not empty retrurn to the top element
        if not self.is_empty():
            return self.head.data
        else:
            print("\nStack is empty")
            return float('-inf')

#create a stack
st = Stack()

st.push(1)
st.push(2)
st.push(3)
st.push(4)

print("The top element is ", st.peek())

print("Remove two elements ")
st.pop()
st.pop()

print("Top element is ", st.peek())

