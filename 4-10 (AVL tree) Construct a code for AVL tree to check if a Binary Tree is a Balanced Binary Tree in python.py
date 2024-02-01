class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def is_balanced(root):
    if root is None:
        return True
    left_height = height(root.left)
    right_height = height(root.right)
    if abs(left_height - right_height) > 1:
        return False
    return is_balanced(root.left) and is_balanced(root.right)

def height(root):
    if root is None:
        return 0
    return max(height(root.left), height(root.right)) + 1
# Testing the code
print("""
        1\n
       / \ \n
      2   3\n
     /   / \ \n
    4   5   6\n
  
""")
r = Node(1)
r.left = Node(2)
r.right = Node(3)
r.left.left = Node(4)
r.left.right = Node(5)
r.right.left = Node(6)


print("Is tree balanced?", is_balanced(r)) 
