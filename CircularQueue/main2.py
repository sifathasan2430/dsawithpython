class CircularQueue:
    def __init__(self,size):
        self.front=self.rare=-1
        self.size=size
        self.items=[None]*self.size

    def Enqueue(self,value):
        if self.rare and self.front ==-1:
            self.rare=self.front=0
            self.items[self.front]=value
        elif ((self.rare+1)%self.size==self.front):
            print("array is full")
        else:
            self.rare=(self.rare+1)%self.size
            self.items[self.rare]=value
        print(self.items)
    def Dequeue(self):
        if self.front and self.rare ==-1:
            print('array is empty')
        elif self.front==self.rare:
            
            self.items[self.front]=None
            self.front=-1
            self.rare=-1
        else:
            self.items[self.front]=None
            self.front=(self.front+1)%self.size
        print(self.items,'dequeue')
obj1=CircularQueue(3)
obj1.Enqueue(10)
obj1.Enqueue(10)
obj1.Enqueue(10)

obj1.Dequeue()
obj1.Dequeue()
obj1.Enqueue(432)
obj1.Enqueue(323)
            