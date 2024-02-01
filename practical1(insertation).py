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
            listr += str(tem.data)+'------>'
            tem = tem.next
        print(listr)
    def insert_at_end(self,data):
        if self.head is None:
            self.head = NODE(data,None)
            return

        tem = self.head
        while tem.next:
            tem = tem.next

        tem.next = NODE(data,None)

    def insert_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana","apple","mango"])

    
    ll.print()



