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

    def remove_at(self,index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid index")
        if index==0:
            self.head=self.head.next
            return
        count = 0
        tem = self.head
        while tem:
            if count == index-1:
                tem.next = tem.next.next
                break

            tem = tem.next
            count += 1

        



        
        '''

        tem = self.head
        while tem.next:
            tem = tem.next

        tem.next = NODE(data,None)
        
'''
if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["Banana","apple","mango","orange","graps"])
    #ll.print()
    #ll.remove_at(2)
    ll.print()



