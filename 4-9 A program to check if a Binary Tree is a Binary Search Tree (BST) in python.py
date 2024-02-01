class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def is_bst(root):
    if root is None:
        return True

    if root.left is not None and root.left.data >= root.data:
        return False

    if root.right is not None and root.right.data <= root.data:
        return False

    return is_bst(root.left) and is_bst(root.right)

# Driver code

# root = Node(5)
# root.left = Node(3)
# root.right = Node(7)

while True:
    r=int(input("Root Node Value: "))
    root = Node(r)
    l=int(input("Left Root Node Value: "))
    if l<=-1:
        break
    else:
        root.left = Node(l)
    rr=int(input("Right Root Node Value: "))
    if rr<=-1:
        break
    else:
        root.right = Node(rr)
    if is_bst(root):
        print("The tree is a BST")
    else:
        print("The tree is not a BST")
