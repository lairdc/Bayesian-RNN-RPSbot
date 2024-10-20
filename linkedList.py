class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_front(self, data):
        """Add a new node to the front of the list in O(1) time."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def to_list(self):
        """Convert the linked list to a Python list (O(n) time, but only when needed)."""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def __getitem__(self, index):
        """Allow indexing for the linked list."""
        current = self.head
        current_index = 0

        while current:
            if current_index == index:
                return current.data
            current = current.next
            current_index += 1

        # If index is out of bounds
        raise IndexError("LinkedList index out of range")

    def __repr__(self):
        """Return a string representation of the linked list in array format."""
        return str(self.to_list())
