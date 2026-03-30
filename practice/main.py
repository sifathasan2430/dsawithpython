class Node:
    def __init__(self,data,next=None):
        self.value=data
        self.next=None

class SingleLinkList:
    def __init__(self):
        self.head=None
    def add_at_the_end(self,data):
        new_node=Node(data)
        pointer=self.head
        if self.head is None:
            self.head=new_node
            return
        while pointer.next !=None:
            pointer=pointer.next
        pointer.next=new_node
    def add_at_the_beg(self,data):
        new_node=Node(data)
        pointer=self.head
        new_node.next=pointer
        
        self.head=new_node
    def add_end_of_the_end(self,data):
        new_node=Node(data)
        pointer=self.head
        while pointer.next !=None:
            pointer=pointer.next
        pointer.next=new_node
    def add_in_the_middle(self,data,list_item):
        new_node=Node(data)
        pointer=self.head
        if pointer.value == list_item:
            new_node.next=pointer.next
            self.head.next=new_node
            return

        while pointer.next !=None:
            if pointer.value == list_item:
                new_node.next=pointer.next
                pointer.next=new_node
                break
            
                
            pointer=pointer.next
        if pointer.value==list_item:
            pointer.next=new_node
    def delete_list(self,list_item):
        
        pointer=self.head
        prev=pointer
        print(pointer.value==list_item)
        if pointer.value==list_item:
            
            self.head=pointer.next
            return
        
        while pointer.next !=None:
            
            if pointer.value==list_item:
                print(pointer.value,prev.value)
                prev.next=pointer.next
                return

            prev=pointer
            pointer=pointer.next
        if pointer.value==list_item:
            prev.next=None
        
        
            






        

    def display(self):
        pointer=self.head
        while pointer.next :
            print(f"{pointer.value} + > {(pointer.next)}")
            pointer=pointer.next
        
        print(pointer.value,pointer.next)
        
        
obj1=SingleLinkList()
obj1.add_at_the_end(10)
obj1.add_at_the_end(20)
obj1.add_at_the_end(30)
obj1.add_at_the_end(40)
obj1.add_at_the_beg(5)
obj1.add_at_the_beg(2)
obj1.add_in_the_middle(8,5)
obj1.add_in_the_middle(25,20)
obj1.add_in_the_middle(45,40)
obj1.delete_list(45)

# obj1.add_end_of_the_end(55)
obj1.display()

         
        