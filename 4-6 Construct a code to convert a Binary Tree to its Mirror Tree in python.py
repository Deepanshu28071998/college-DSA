class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def mirror(root):
  if root is None:
    return

  mirror(root.left)
  mirror(root.right)

  temp = root.left
  root.left = root.right
  root.right = temp

def printInorder(root):
  if root is None:
    return

  printInorder(root.left)
  print(root.data)
  printInorder(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Inorder traversal of the original tree")
printInorder(root)

mirror(root)

print("\nInorder traversal of the mirror tree")
printInorder(root)
