class que:
    def __init__(self):
        self.items=[]
# class enqueue:
    def enque(self,item):
        self.items.insert(0,item)
# class dequeue:
    def deque(self):
        return self.items.pop()
    def trav(self):
        for i in self.items:
            print(i)
            #q = que()

    def is_empty(self):
        return len(self.items)==0
    def size(self):
        return len(self.items)
    
q=que()
while True:
    print("\nQueue Operations: ")
    print("1 for 'Insert the value'")
    print("2 for 'Delete the value'")
    print("3 for 'Traverse the Queue'")
    print("4 for 'Quit'")
    choice = input("Enter your choice: ")
    if choice =='1':
        item=input("Enter data to Append: ")
        q.enque(item)
    elif choice=='2':
        # key=input("Enter key to Delete: ")
        q.deque()
    elif choice=='3':
        q.trav()
    elif choice=='4':
        break
    else:
        print("Invalid choice")
   