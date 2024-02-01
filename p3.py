class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class cll:
    def __init__(self):
        self.head=None
    def empty(self):
        return self.head is None
    def insert_at_beg(self,data):
        newnode=Node(data)
        if self.empty():
            self.head=newnode
            newnode.next=self.head
        else:
            tmp=self.head
            while tmp.next!=self.head:
                tmp=tmp.next
            newnode.next=self.head
            self.head=newnode
            tmp.next=newnode
    def insert_at_end(self,data):
        newnode=Node(data)
        if self.empty():
            self.head=newnode
            newnode.next=self.head
        else:
            tmp=self.head
            while tmp.next!=self.head:
                tmp=tmp.next
            newnode.next=self.head
            tmp.next=newnode
    def delete_at_beg(self):
        if self.empty():
            print("List is empty!")
        else:
            if self.head.next==self.head:
                self.head=None
            else:
                tmp=self.head
                while tmp.next!=self.head:
                    tmp=tmp.next
                tmp.next=self.head.next
                self.head=tmp.next
    def delete_at_end(self):
        if self.empty():
            print("List is empty!")
        else:
            if self.head.next==self.head:
                self.head=None
            else:
                prv=None
                tmp=self.head
                while tmp.next!=self.head:
                    prv=tmp
                    tmp=tmp.next
                prv.next=self.head
    def traverse(self):
        if self.empty():
            print("List is empty!")
        else:
            tmp = self.head
            while tmp:
                print(tmp.data,end="--->")
                tmp=tmp.next
                if tmp==self.head:
                    break
            print("Null list")
def main():
    c=cll()
    while True:
        print("------MENU------")
        print("1 for 'INSERT AT BEGINNING'")
        print("2 for 'INSERT AT END'")
        print("3 for 'DELETE AT BEGINNING'")
        print("4 for 'DELETE AT END'")
        print("5 for 'TRAVERSE'")
        print("6 for 'EXIT'")
        choice=int(input("Enter Yor Choice: "))
        if choice==1:
            data=int(input("Enter data to 'INSERT': "))
            c.insert_at_beg(data)
        elif choice==2:
            data=int(input("Enter data to 'INSERT AT END': "))
            c.insert_at_end(data)
        elif choice==3:
            c.delete_at_beg()
        elif choice==4:
            c.delete_at_end()
        elif choice==5:
            c.traverse()
        elif choice==6:
            break
        else:
            print("'INVALID CHOICE!'")

            
if __name__=="__main__":
    main()
