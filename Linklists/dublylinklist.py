class Node:
    def __init__(self,data,next=None,prev=None):
        self.prev=prev
        self.data=data
        self.next=next

class DoublyLinkList:
    def __init__(self):
        self.head=None
    def add_end(self,value):
        
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            return
        pointer=self.head
        
        while pointer.next !=None:

            pointer=pointer.next
        pointer.next=new_node
        new_node.prev=pointer
    def add_beg(self,value):
        new_node=Node(value)
        # self.head=new_node if write this early that will make balender.we cannot access the full dublylinklist
       
        new_node.prev=None
        new_node.next=self.head
        self.head.prev=new_node
        self.head=new_node


        # wrong
        # new_node.next=self.head
        # self.head.prev=new_node
        # self.head=new_node
        
    

        # self.head=new_node
        
        
        # self.head=new_node
    def add_middle(self,value,list):
        new_node=Node(value)
        pointer=self.head
        while pointer.next !=None:
            if pointer.data==list:
                new_node.prev=pointer
                new_node.next=pointer.next
                pointer.next.prev=new_node
                pointer.next=new_node

                break

            pointer=pointer.next
    def delete_list(self,x):
        pointer=self.head
        if pointer.data==x:
            pointer.next.prev=None
            self.head=pointer.next
            return
        while pointer.next !=None:
            if pointer.data ==x:
                print(pointer.next.data,"this1")
                print(pointer.data,"this2")
                
                pointer.next.prev=pointer.prev
                pointer.prev.next=pointer.next
                
                return
            pointer=pointer.next
        if pointer.data==x:
            pointer.prev.next=None
            
        
        
       
        

        

    def chain_test(self):
        pointer=self.head
        while pointer.next !=None:
            print(id(pointer),'pointer')
            print(id(pointer.next),'pointer.next')
            print(id(pointer.next.prev),"pointer.next.prev")
            
            pointer=pointer.next
       

    def display(self):
       pointer = self.head
       elements = []
       while pointer:
            elements.append(str(pointer.data))
            pointer = pointer.next
       print("Forward:  " + " <-> ".join(elements) + " -> None")

obj=DoublyLinkList()
obj.add_end(10)
obj.add_end(20)

obj.add_end(30)
obj.add_end(40)
obj.add_end(50)
obj.add_beg(5)
obj.add_beg(99)
obj.add_middle(420,40)
obj.delete_list(50)
obj.chain_test()
obj.display()
# obj.display_reverse()