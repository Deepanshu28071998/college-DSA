'''

class NODE:
    def __init__(self,data,ref):
        self.data=data
        self.ref=ref
    def info(self):
        print(f"{self.data} and next data is {self.ref}")
a = NODE(10,20)
a.info()
b = NODE(20,30)
b.info()
c = NODE(30,40)
c.info()
d = NODE(40,50)
d.info()
'''
'''
class LinkedList:
    def __init__(self):
        self.head=None
    def print_LL(self):
        if self.head is None:
            print("The LinkedList is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n= n.ref
            
            
LL1 = LinkedList()
LL1.print_LL()

'''




'''
        temp=self.head
        while (temp):
            print(temp.data)
            temp=temp.next
    def insert_at_begin(self,data):
        new_node = NODE(data)
        new_node.next=self.head
        self.head = new_node
    def insert_at_begin(self,data):
        new_node = NODE(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self,data):
        new_node = NODE(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while (last_node.next):
            last_node = last_node.next
        last_node.next = new_node

    def insert_after_node(self,prev_node, data):
        if not prev_node:
            print("Previous node is not in the list")
            return
        new_node = NODE(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self,key):
'''        
'''
node1= NODE(10)
print(node1)
'''
#Traversal Method in Linked List:-
'''
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def print_list(self):
    temp = self.head
    while (temp):
      print(temp.data)
      temp = temp.next

  def append(self, data):
    new_node = Node(data)
    if (self.head is None):
      self.head = new_node
      return
    last_node = self.head
    while (last_node.next):
      last_node = last_node.next
    last_node.next = new_node

# Driver program for testing
llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.print_list()
'''




#class & object & constructor:-
'''
class person():
    def __init__(self,n,o):
        print("hello")
        self.name = n
        self.occ = o
    def info(self):
        print(f"I am {self.name} the {self.occ}")
a = person("Deepanshu","PM")
a.info()
b = person("Harsh","TL")
b.info()
c = person(1,2)
c.info()
'''
'''
    name = "Deepanshu Jain"
    occ = "Project Manager"
    def info (self):
        print(f"{self.name} is {self.occ}")
'''

'''
pm = person()
pm.info()
a = person()
a.name = "Vaibhav"
a.occ = "client"
#a.info()
#print(a.name,"is our",a.occ)
b = person()
b.name="Harsh"
b.occ="Team Leader"
#b.info()
c = person()
c.name="Deepak"
c.occ="Developer"
#c.info()
#print(b.name,"is",c.occ)
a.info()
b.info()
c.info()
'''




######Right way to write a Linked List:-
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

###right way to write the values in linked list:-
## in this method the list is creating a begining and the end part:-
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
        

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_begining(5)
    ll.insert_at_begining(8)
    ll.insert_at_begining(10)
    ll.insert_at_begining(12)
    ll.insert_at_begining(18)
    ll.insert_at_end(79)
    ll.print()



'''




###right way to write the values in linked list:-
## in this method the list is creating the end part:-
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
        

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_end(5)
    ll.insert_at_end(8)
    ll.insert_at_end(10)
    ll.insert_at_end(12)
    ll.insert_at_end(18)
    ll.insert_at_end(79)
    ll.print()

'''


'''
#Traversing LinkedList
class Node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None
class SLinkedList:
    def __init__(self):
        self.headval=None
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval
            list = SLinkedList()
            list.headval = Node("Mon")
            e2 = Node("Tue")
            e3 = Node("Wed")

            list.headval.nextval=e2
            e2.nextval=e3
            list.listprint()


'''






#wrong
#mam
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
    list.headval = Node("Mon")
    e2 = Node("Tue")
    e3 = Node("Wed")
    list.headval.nextval = e2
    e2.nextval = e3
    list.listprint()
'''
