class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

class SingleLinkList:
    def __init__(self):
        self.head=None
    def insert_End(self,value):
        new_node=Node(value)
        if self.head ==None:
            # print('self.head')
            self.head=new_node
            
        else:
            # print('not none')
            pointer=self.head
            while pointer.next:
                pointer=pointer.next
            pointer.next=new_node
    def insert_first(self,value):
        new_node=Node(value)
        new_node.next=self.head
        self.head=new_node
    def insert_middle(self,value,middle_value):
    
        new_node=Node(value)
        pointer=self.head
        
        while pointer:
            # print("loop running",pointer.data==20)
            # print(middle_value,'middle value')
            if pointer.data==middle_value:
                # print('data is found')
                new_node.next=pointer.next
                pointer.next=new_node
                return
            
            pointer=pointer.next
        print("no data found")
    def delete_value(self,value):
        pointer=self.head
        
        prev=pointer
        if pointer.data==value:
            self.head=pointer.next
        while pointer:
            print(f"{pointer.data}:{pointer.next}")
            # if pointer.data==value:
            
                
            #     print(pointer.data,'insideifelse')
                

            #     return
            

            # prev=pointer.next

            # pointer=pointer.next
          
            if pointer.data==value:
                
                prev.next=pointer.next
                break
            
            prev=pointer

            pointer=pointer.next
        # print(pointer.data,'this is pointer data')
        if (pointer.data==value):
            pointer.next=prev.next


        
        
        

    def display(self):
        pointer=self.head
        while pointer:
            print(pointer.data,end="> ")

            pointer=pointer.next
        print("None")

obj=SingleLinkList()
obj.insert_End(20)
obj.insert_End(30)
obj.insert_End(40)
obj.insert_End(50)
obj.insert_End(60)
obj.insert_End(70)
obj.insert_End(80)
# obj.insert_first(11111111122222222)
# obj.insert_middle(99,1)
# obj.delete_value(99)
# obj.insert_End(2)
# # obj.insert_End(3)
# obj.insert_End(4)
# obj.insert_End(5)
# obj.insert_End(6)
# obj.delete_value(50)
obj.delete_value(80)
obj.display()
