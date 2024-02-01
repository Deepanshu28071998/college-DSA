class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorder(root):
    if root is None:
        return
    print(root.value)
    preorder(root.left)
    preorder(root.right)

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.value)
    inorder(root.right)

def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.value)

# Example usage
root = Node(1)
root.left = Node(2)
root.right = Node(3)

print("Preorder traversal:")
preorder(root)

print("Inorder traversal:")
inorder(root)

print("Postorder traversal:")
postorder(root)
