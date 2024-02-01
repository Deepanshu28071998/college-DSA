class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
class LL:
    def __init__(self):
        self.head=None
    def insert(self,data):
        if not self.head:
            self.head=node(data)
        else:
            tem=self.head
            while tem.next:
                tem=tem.next
            tem.next=node(data)
    
    def deletell(self,data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        tem=self.head
        while tem.next:
            if tem.next.data==data:
                tem.next=tem.next.next
                return
            tem=tem.next
    def traversell(self):
        tem=self.head
        print("The Linked List is: ")
        while tem:
            print(tem.data,end=" ")
            tem=tem.next
        print()
linked_list = LL()
while True:
    print("1 for INSERT a NODE: ")
    print("2 for DELETE a NODE: ")
    print("3 for TRAVERSE the LINKED LIST")
    print("4 for QUIT")
    choice=int(input("Enter your choice: "))
    if choice ==1:
        data=int(input("Enter the value to 'Insert' in Linked List: "))
        linked_list.insert(data)
    elif choice==2:
        data=int(input("Enter the value to 'Delete' in Linked List: "))
        linked_list.deletell(data)
    elif choice==3:
         linked_list.traversell()
    elif choice==4:
         break
    else:
         print("Invalid choice")
            

               

               
            

                
