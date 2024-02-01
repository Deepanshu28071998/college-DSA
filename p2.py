class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class doublell:
    def __init__(self):
        self.head=None
    def append(self,data):
        newn=node(data)
        if self.head is None:
            self.head=newn
        else:
            curn=self.head
            while curn.next:
                curn=curn.next
            curn.next=newn
            newn.prev=curn
    def deln(self,key):
        curn=self.head
        while curn:
            if curn.data==key and curn ==self.head:
                if not curn.next:
                    curn=None
                    self.head=None
                    return
                else:
                    nxtn=curn.next
                    curn.next=None
                    nxtn.prev=None
                    curn=None
                    self.head=nxtn
                    return
            elif curn.data==key:
                if curn.next:
                    nxtn=curn.next
                    prev=curn.prev
                    prev.next=nxtn
                    nxtn.prev=prev
                    curn.next=None
                    curn.prev=None
                    curn=None
                    return
                else:
                    prev=curn.prev
                    prev.next=None
                    curn.prev=None
                    curn=None
                    return
            curn=curn.next
        
    def traversell(self):
        curn=self.head
        while curn:
            print(curn.data)
            curn=curn.next
dll=doublell()
while True:
    print("\nDouble Linked List Operations: ")
    print("1 for 'Append'")
    print("2 for 'Delete'")
    print("3 for 'Traverse'")
    print("4 for 'Quit'")
    choice = input("Enter your choice: ")
    if choice =='1':
        data=input("Enter data to Append: ")
        dll.append(data)
    elif choice=='2':
        key=input("Enter key to Delete: ")
        dll.deln(key)
    elif choice=='3':
        dll.traversell()
    elif choice=='4':
        break
    else:
        print("Invalid choice")
                
                
