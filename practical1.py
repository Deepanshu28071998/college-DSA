'''
class NODE:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self,data):
        node=NODE(data,self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked List is Blank")
            return
        tem = self.head
        listr = ''
        while tem:
            listr += str(tem.data)+'-->'
            tem = tem.next
        print(listr)
        


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_begining(5)
    ll.insert_at_begining(8)
    ll.insert_at_begining(10)
    ll.insert_at_begining(12)
    ll.insert_at_begining(18)
    
    ll.print()
'''

'''
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(data)
    def delete(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        temp = self.head
        while temp.next:
            if temp.next.data == data:
                temp.next = temp.next.next
                return
            temp = temp.next
    def traverse(self):
        temp = self.head
        print("The Linked List : ")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()
linked_list = LinkedList()
while True:
    print("1. Insert")
    print("2. Delete")
    print("3. Traverse")
    print("4. Quit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        data = int(input("Enter the value to insert : "))
        linked_list.insert(data)
    elif choice == 2:
        data = int(input("Enter the value to delete : "))
        linked_list.delete(data)
    elif choice == 3:
        linked_list.traverse()
    elif choice == 4:
        break
    else:
        print("Invalid choice")
'''



class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None
class SLinkedList:
   def __init__(self):
      self.headval = None
   def listprint(self):
      printval = self.headval
      while printval is not None:
         print (printval.dataval)
         printval = printval.nextval
list = SLinkedList()
list.headval = Node("apple")
e2 = Node("graps")
e3 = Node("orange")
e4 = Node("mango")
e5 = Node("dragunfruit")
# Link first Node to second node
list.headval.nextval = e2
# Link second Node to third node
e2.nextval = e3
#list.e2.nextval = e3
e3.nextval = e4
#list.e4.nextval = e5
e4.nextval = e5
#list.headval.nextval = e2
#list.headval.nextval = e2
list.listprint()





