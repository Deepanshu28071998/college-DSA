class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end="--->")
            current = current.next
        print()

def merge_sorted_lists(list1, list2):
    if not list1:
        return list2
    # else:
    #     return list1
    
    elif not list2:
        return list1
    
    

    merged_list = None

    if list1.data < list2.data:
        merged_list = list1
        merged_list.next = merge_sorted_lists(list1.next, list2)
    else:
        merged_list = list2
        merged_list.next = merge_sorted_lists(list1, list2.next)

    return merged_list

def main():
    list1 = LinkedList()
    list2 = LinkedList()

    print("Enter list1:")
    while True:
        inp = input()
        if inp:
            list1.append(int(inp))
        else:
            break

    print("Enter list2:")
    while True:
        inp = input()
        if inp:
            list2.append(int(inp))
        else:
            break

    print("Merged list:")
    merged_list = merge_sorted_lists(list1.head, list2.head)
    merged_list.print_list()

if __name__ == "__main__":
    main()
