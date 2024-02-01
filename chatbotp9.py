# Node class to represent a node in the linked list
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

# Function to merge two sorted linked lists
def merge_sorted_lists(head1, head2):
    # Create a dummy node and initialize it as None
    dummy = Node()
    # Create a pointer to the dummy node
    tail = dummy

    # Traverse both linked lists and compare the nodes
    while head1 is not None and head2 is not None:
        # Compare the data of the nodes and append the smaller one to the merged list
        if head1.data <= head2.data:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next
        # Move the tail pointer to the next node
        tail = tail.next

    # Append the remaining nodes of the first linked list, if any
    while head1 is not None:
        tail.next = head1
        head1 = head1.next
        tail = tail.next

    # Append the remaining nodes of the second linked list, if any
    while head2 is not None:
        tail.next = head2
        head2 = head2.next
        tail = tail.next

    # Return the merged linked list by skipping the dummy node
    return dummy.next

# Function to print the linked list
def print_linked_list(head):
    current = head
    while current is not None:
        print(current.data, end="--->")
        current = current.next
    print()

# Create two sorted linked lists
# First linked list: 1 -> 3 -> 5 -> 7 -> 9
head1 = Node(1)
head1.next = Node(3)
head1.next.next = Node(5)
head1.next.next.next = Node(7)
head1.next.next.next.next = Node(9)

# Second linked list: 2 -> 4 -> 6 -> 8 -> 10
head2 = Node(2)
head2.next = Node(4)
head2.next.next = Node(6)
head2.next.next.next = Node(8)
head2.next.next.next.next = Node(10)

# Merge the two sorted linked lists
merged_head = merge_sorted_lists(head1, head2)

# Print the merged linked list
print("Merged Linked List:")
print_linked_list(merged_head)
