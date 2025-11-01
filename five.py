class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, data):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = self.insert(root.left, data)
        elif data > root.data:
            root.right = self.insert(root.right, data)
        return root

    def search(self, root, key):
        if root is None:
            return False
        if root.data == key:
            return True
        elif key < root.data:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    def find_min(self, root):
        while root.left:
            root = root.left
        return root

    def delete(self, root, key):
        if root is None:
            return None
        if key < root.data:
            root.left = self.delete(root.left, key)
        elif key > root.data:
            root.right = self.delete(root.right, key)
        else:
            # Node found - handle 3 cases
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            # Node with two children
            temp = self.find_min(root.right)
            root.data = temp.data
            root.right = self.delete(root.right, temp.data)
        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)


bst = BST()
root = None

print("Nishanth, 24217, CSE-C")
n = int(input("Enter number of elements to insert in BST: "))
for i in range(n):
    val = int(input(f"Enter value {i+1}: "))
    root = bst.insert(root, val)

print("Inorder traversal of BST:")
bst.inorder(root)
print()

key = int(input("Enter value to search: "))
found = bst.search(root, key)
print("Element found." if found else "Element not found.")

key = int(input("Enter value to delete: "))
root = bst.delete(root, key)

print("Inorder traversal after deletion:")
bst.inorder(root)
print()

