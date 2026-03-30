class CircularQueue:
    def __init__(self,size):
        self.front=self.rare=-1
        self.size=size
        self.items=[None]*size
    def Enqueue(self,value):
        print((self.rare+1)%self.size ==self.front,(self.rare+1)%self.size,self.front)
        if ((self.rare+1)%self.size ==self.front):
            print("Queue is Full and its based when its full")
        # elif self.rare and self.front == -1:
        elif self.rare == -1:
          
            self.front=self.rare=0
            print(self.rare,self.front)
            
            self.items[self.rare]=value
            print(self.items,'when it is one first zero element')
        else:
            self.rare=(self.rare+1)%self.size
            self.items[self.rare]=value
            print(self.items,'when it as use all')
    def Dequeue(self):
        if self.front and self.rare==-1:
            print("queue is empty")
           
        elif self.front == self.rare:
            print(self.items,'when front and rare is same',self.front,self.rare,'before')
            # self.front=self.rare=-1
            self.items[self.front]=None
            self.front=self.rare=-1
            print(self.items,'when front and rare is same',self.front,self.rare)
        else:
            print(self.front,self.rare,'de2')
            # self.front=(self.front+1)%self.size 
            self.items[self.front]=None
            self.front=(self.front+1)%self.size
            print(self.items,"dequeue2")
#obj1=CircularQueue(6)
# obj1.Enqueue(20)
# obj1.Enqueue(20)
# obj1.Enqueue(20)
# obj1.Enqueue(20)
# obj1.Enqueue(20)
# obj1.Enqueue(20)
# obj1.Enqueue(20)
# obj1.Dequeue()
obj2=CircularQueue(5)
obj2.Enqueue(10)
obj2.Enqueue(20)
# obj2.Enqueue(30)
# obj2.Enqueue(40)
# obj2.Enqueue(50)
# obj2.Enqueue(20)
obj2.Dequeue()
obj2.Dequeue()
obj2.Dequeue()
