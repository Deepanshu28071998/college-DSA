class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = new_node
            new_node.prev = curr_node

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete(self, data):
        curr_node = self.head
        while curr_node:
            if curr_node.data == data:
                if curr_node.prev:
                    curr_node.prev.next = curr_node.next
                    if curr_node.next:
                        curr_node.next.prev = curr_node.prev
                else:
                    self.head = curr_node.next
                    if self.head:
                        self.head.prev = None
                return
            curr_node = curr_node.next

    def traverse(self):
        result = []
        curr_node = self.head
        while curr_node:
            result.append(curr_node.data)
            curr_node = curr_node.next
        return result

# Example usage:
dllist = DoublyLinkedList()
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.prepend(0)
dllist.delete(2)
print(dllist.traverse())  # Output: [0, 1, 3]
