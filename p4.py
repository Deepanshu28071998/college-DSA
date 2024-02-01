class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def revlist(head):
    prv=None
    cur=head
    while cur:
        n_n=cur.next
        cur.next=prv
        prv=cur
        cur=n_n
    return prv
def printlist(head):
    if head is None:
        print("List is empty!")
        return
    node=head
    while node:
        print(node.data,end="--->")
        node=node.next
    print("Null list")
def main():
    head=None
    while True:
        print("-----MENU----")
        print("1 for 'CREATE LIST'")
        print("2 for 'REVERSE LIST'")
        print("3 for 'PRINT LIST'")
        print("4 for 'EXIT'")
        choice=int(input("Enter your choice: "))
        if choice ==1:
            data=int(input("Enter the Integer value for creating a linked list"))
            node =Node(data)
            if head is None:
                head=node
            else:
                tmp=head
                while tmp.next:
                    tmp=tmp.next
                tmp.next=node
        elif choice==2:
            head = revlist(head)
        elif choice==3:
            printlist(head)
        elif choice==4:
            break
        else:
            print("INVALID CHOICE! PLEASE ENTER A VALID KEY.")
if __name__=="__main__":
    main()
            
