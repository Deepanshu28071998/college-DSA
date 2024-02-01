class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

class BinarySearchTree:
  def __init__(self):
    self.root = None

  def insert(self, val):
    if self.root is None:
      self.root = Node(val)
      return
    self._insert(val, self.root)

  def _insert(self, val, curr_node):
    if val < curr_node.val:
      if curr_node.left is None:
        curr_node.left = Node(val)
        return
      self._insert(val, curr_node.left)
    else:
      if curr_node.right is None:
        curr_node.right = Node(val)
        return
      self._insert(val, curr_node.right)

  def search(self, val):
    return self._search(val, self.root)

  def _search(self, val, curr_node):
    if curr_node is None:
      return False
    if val == curr_node.val:
      return True
    if val < curr_node.val:
      return self._search(val, curr_node.left)
    return self._search(val, curr_node.right)

  def print_tree(self):
    self._print_tree(self.root)

  def _print_tree(self, curr_node):
    if curr_node is None:
      return
    self._print_tree(curr_node.left)
    print(curr_node.val)
    self._print_tree(curr_node.right)

my_tree = BinarySearchTree()
print("insert the number:",5)
my_tree.insert(5)
print("tree")
my_tree.print_tree()
print("---")
print("insert the number:",3)
my_tree.insert(3)
print("tree")
my_tree.print_tree()
print("---")
print("insert the number:",7)
my_tree.insert(7)
print("tree")
my_tree.print_tree()
print("---")
print("insert the number:",2)
my_tree.insert(2)
print("tree")
my_tree.print_tree()
print("---")
print("insert the number:",1)
my_tree.insert(1)
print("tree")
my_tree.print_tree()
print("---")
print("insert the number:",4)
my_tree.insert(4)
print("tree")
my_tree.print_tree()
print("---")
print("insert the number:",6)
my_tree.insert(6)
print("tree")
my_tree.print_tree()
print("---")
print("insert the number:",8)
my_tree.insert(8)
print("tree")
my_tree.print_tree()
print("---")


print("The final binary tree is:")
my_tree.print_tree()
