class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def print_paths(root):
    if root is None:
        return

    path = []
    print_paths_recursive(root, path)

def print_paths_recursive(root, path):
    if root is None:
        return

    path.append(root.data)

    if root.left is None and root.right is None:
        print(path)
        return

    print_paths_recursive(root.left, path)
    print_paths_recursive(root.right, path)

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print_paths(root)
