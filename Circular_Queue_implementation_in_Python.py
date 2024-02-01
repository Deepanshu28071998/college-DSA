#circular Queue
# Circular Queue implementation in Python
class mcq():
    def __init__(self, size):
        self.size=size
        self.qu=[None]*size
        self.front=self.rear=-1
    def enqu(self,data):
        if ((self.rear+1)%self.size==self.front):       #if our size of circular queue is 5 then value of rear is 5+1=6. And size of queue is 5. then we apply the modulus operation between the rear and size it will give the value = to the front. (5+1)%5==1 
            print("The Circular Queue is Full\n")
        elif (self.front==-1):
            self.front=0
            self.rear=0
            self.qu[self.rear]=data
        else:
            self.rear=(self.rear+1)%self.size
            self.qu[self.rear]=data
    def deque(self):
        if(self.front==-1):
            print("Circular Queue is Empty\n")
        elif (self.front==self.rear):
            temp = self.qu[self.front]
            self.front = -1
            self.rear = -1
            return temp
        else:
            temp = self.qu[self.front]
            self.front = (self.front + 1) % self.size
            return temp
    def printCQ(self):
        if(self.front == -1):
            print("Circular Queue is Empty")
        elif (self.rear>=self.front):
            for i in range(self.front,self.rear+1):
                print(self.qu[i],end=" ")
            print()
        else:
            for i in range(self.front,self.size):
                print(self.qu[i],end=" ")
            for i in range(0,self.rear+1):
                print(self.qu[i],end=" ")
            print()
obj=mcq(5)
obj.enqu(1)
obj.enqu(2)
obj.enqu(3)
obj.enqu(4)
obj.enqu(5)
print("Initial Queue")
obj.printCQ()

obj.deque()
print("After removing an element from the queue")
obj.printCQ()