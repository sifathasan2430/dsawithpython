class Stack:
    def __init__(self):
        self.array=[]
    def push(self,data):
        self.array.insert(0,data)
        
    def length(self):
        return len(self.array)
    def pop(self):
        return self.array.pop(0)
    def peek(self):
        if len(self.array)==0:
            raise Exception("stack is empty")
        else:
            print(self.array[0])
    def display(self):
        print(self.array)
obj=Stack()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
obj.push(5)
print(obj.pop())
obj.peek()
obj.display()
