class Node:
    count=0
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
        Node.count+=1
    
class SingleLinkList:
    
    def __init__(self):
        self.head=None
    def insert_end(self,value):
        new_node=Node(value)
        # print(Node.count)
        # print(new_node.data)
        if self.head is None:
            self.head=new_node
            return
        pointer=self.head
        # print(pointer.data,'this is pointer')
        while pointer.next !=None:
            # pointer.next=new_node [wrong]
            pointer=pointer.next

        pointer.next=new_node
        # print(pointer.data,'this is when itertion is complete')
    def insert_first(self,value):
            new_node=Node(value)
            new_node.next=self.head
            self.head=new_node
    def insert_any_where(self,value,listitem):
        new_node=Node(value)
        pointer=self.head
        if pointer.data==listitem:
            new_node.next=self.head
            self.head=new_node
            return
        
        while pointer.next != None:
            
            if pointer.data ==listitem:
                new_node.next=pointer.next  
                pointer.next=new_node
                
            
            
            pointer=pointer.next
        if pointer.data==listitem:
            pointer.next=new_node
            print(f'{pointer.data}:{pointer.next}')
    def delete_list(self,list):
        pointer=self.head
        prev=pointer
        if (pointer.data==list):
            self.head=prev.next
        
        while pointer.next !=None :
            print(f"{pointer.data} prev:{prev.data}")
            if pointer.data==list:
                print(f"{pointer.data} prev:{prev.data}")
                prev.next=pointer.next
                # prev.next=pointer.next
                print('pointer',pointer.data)
                break
            else:
                prev=pointer
            pointer=pointer.next
        if pointer.data==list:
            print(f"{pointer.data}:{prev.data}")
            prev.next=None
            

            
    def middle_value_finder(self,value):
        total_node=Node.count
        print(total_node)
        pointer=self.head
        while pointer.next != None:
            if pointer.data==value:
                return f"Node with value{pointer.data}"

            pointer=pointer.next        
            
            
            


            
    def display(self):
        pointer=self.head
        # print(pointer.data)
        while pointer != None:

            print(f"{pointer.data}",end='>')
            pointer=pointer.next
        print("None")
obj=SingleLinkList()


obj.insert_end(1)
obj.insert_end(2)
obj.insert_end(3)
obj.insert_end(4)
obj.insert_end(5)
print(obj,'this is singly link this')
# obj.insert_end(60)
# obj.insert_end(70)
# obj.insert_first(5)
# obj.insert_any_where(65,60)
# obj.insert_any_where(6,5)
# obj.insert_any_where(55,50)
# obj.insert_any_where(75,70)
# obj.delete_list(75)
# print(obj.head)

obj.display()
result=obj.middle_value_finder(3)
print(result)
class CircularList:
    def __init__(self):
        
        self.head=None
    def add_beg(self,value):
        new_node=Node(value)
        if self.head is None:
            new_node.next=self.head
            self.head=new_node
            return
        pointer=self.head
        while pointer.next !=self.head:

            pointer=pointer.next
        pointer.next=new_node
        
