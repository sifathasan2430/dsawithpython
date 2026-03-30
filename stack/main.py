class Stack:
    def __init__(self):
        self.array=[]
    def length(self):
        return len(self.array)
    def push(self,data):
        
        self.array.append(data)
            
    def delete_stack(self):
        self.array.pop()
    def peek(self):
        print(self.array)
        if len(self.array)==0:
            raise Exception("Stack is empty")
        else:
            print(self.array[(len(self.array)-1)])
        
obj=Stack()

obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
obj.push(5)
obj.push(6)
obj.peek()
obj.delete_stack()
obj.peek()

# obj.push(2)
# obj.push(3)
# obj.push(4)
# obj.push(5)
# obj.push(6)
# obj.push(7)



