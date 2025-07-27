class ArrayOperations:
    def __init__(self):
        self.array = []
        print("Initialized an empty array.")

    def insert(self, index, element):
        if 0 <= index <= len(self.array):
            self.array.append(None)
            for i in range(len(self.array) - 1, index, -1):
                self.array[i] = self.array[i - 1]
            self.array[index] = element
            print(f"Inserted {element} at index {index}.")
        else:
            print(f"Error: Index {index} is out of bounds. Valid range: 0 to {len(self.array)}.")

    def delete(self, index):
        if not self.array:
            print("Error: Array is empty, cannot delete.")
            return

        if 0 <= index < len(self.array):
            deleted_element = self.array[index]
            for i in range(index, len(self.array) - 1):
                self.array[i] = self.array[i + 1]
            self.array = self.array[:-1]
            print(f"Deleted '{deleted_element}' from index {index}.")
        else:
            print(f"Error: Index {index} is out of bounds. Valid range: 0 to {len(self.array) - 1}.")

    def traverse(self):
        if not self.array:
            print("Array is empty.")
            return
        print("Array elements:", end=" ")
        for element in self.array:
            print(element, end=" ")
        print()

    def size(self):
        current_size = len(self.array)
        print(f"Array size: {current_size}")
        return current_size

    def update(self, index, new_element):
        if not self.array:
            print("Error: Array is empty, cannot update.")
            return

        if 0 <= index < len(self.array):
            old_element = self.array[index]
            self.array[index] = new_element
            print(f"Updated index {index} from '{old_element}' to '{new_element}'.")
        else:
            print(f"Error: Index {index} is out of bounds. Valid range: 0 to {len(self.array) - 1}.")


if __name__ == "__main__":
    my_array = ArrayOperations()
    print("-" * 20)

    my_array.size()
    print("-" * 20)

    my_array.insert(0, 10)
    my_array.insert(1, 20)
    my_array.insert(2, 30)
    my_array.insert(1, 15)
    my_array.traverse()
    my_array.size()
    print("-" * 20)

    my_array.insert(10, 99)
    print("-" * 20)

    my_array.update(2, 25)
    my_array.traverse()
    print("-" * 20)

    my_array.update(5, 99)
    print("-" * 20)

    my_array.delete(1)
    my_array.traverse()
    my_array.size()
    print("-" * 20)

    my_array.delete(5)
    print("-" * 20)

    my_array.traverse()
