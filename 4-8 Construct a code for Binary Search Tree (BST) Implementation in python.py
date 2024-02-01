class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        new_node = Node(key)
        if self.root is None:
            self.root = new_node
            return
        current = self.root
        while True:
            if key < current.key:
                if current.left is None:
                    current.left = new_node
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    break
                current = current.right

    def search(self, key):
        current = self.root
        while current is not None:
            if key == current.key:
                return current
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return None

    def min_value(self):
        current = self.root
        while current.left is not None:
            current = current.left
        return current.key

    def max_value(self):
        current = self.root
        while current.right is not None:
            current = current.right
        return current.key

    def print_tree(self):
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            print(current.key, end=" ")
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)

bst = BinarySearchTree()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(8)

print("Inorder traversal of the binary search tree is:")
bst.print_tree()

print("\nMinimum value in the binary search tree is:", bst.min_value())
print("Maximum value in the binary search tree is:", bst.max_value())

search_key = 7
if bst.search(search_key) is not None:
    print(search_key, "is found in the binary search tree.")
else:
    print(search_key, "is not found in the binary search tree.")
