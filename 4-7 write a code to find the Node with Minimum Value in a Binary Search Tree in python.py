from typing import List


class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

# Give a binary search tree and a number,
# inserts a new node with the given number
# in the correct place in the tree. Returns
# the new root pointer which the caller should then use
# (the standard trick to avoid using reference parameters).


def insert(node: Node, data: int) -> Node:

	# If the tree is empty, return a new, single node
	if not node:
		return Node(data)

	# Otherwise, recur down the tree
	if data <= node.data:
		node.left = insert(node.left, data)
	else:
		node.right = insert(node.right, data)

	# Return the (unchanged) node pointer
	return node

# Given a non-empty binary search tree, inorder traversal for
# the tree is stored in the list sorted_inorder. Inorder is LEFT,ROOT,RIGHT.


def inorder(node: Node, sorted_inorder: List[int]) -> None:

	if not node:
		return

	# First recur on left child
	inorder(node.left, sorted_inorder)

	# Then insert the data of node
	sorted_inorder.append(node.data)

	# Now recur on right child
	inorder(node.right, sorted_inorder)


if __name__ == '__main__':
	root = None
	root = insert(root, 4)
	insert(root, 2)
	insert(root, 1)
	insert(root, 3)
	insert(root, 6)
	insert(root, 4)
	insert(root, 5)

	sorted_inorder = []
	inorder(root, sorted_inorder) # calling the recursive function

	# Values of all nodes will appear in sorted order in the list sorted_inorder
	print(f"Minimum value in BST is {sorted_inorder[0]}")
