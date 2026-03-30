
    
    

# node1=Node(20)
# node2=Node(24)
# node3=Node(30)
# print(f'node1:{node1},node2:{node2},node3:{node3}')
# node1.next=node2
# node2.next=node3

# print(node1.data,node1.next,'-----------------------')
# print(node1.data)
# print(node1.next.data)

# print('\n',node1.next.next.data)
# print("how many object create",Node.count)
class Node:
    
    def __init__(self,data):
        self.data=data
        self.next=None
class Linklists:
    count=0
    def __init__(self):
        self.head=None
        Linklists.count+=1

    def insertEndList(self,data):  
        new_node=Node(data)
        print(new_node)
        # if link is not created
        if self.head ==None:
            print("first create")
            self.head=new_node
            return
        current_node=self.head

        while current_node.next !=None:
            # it is the connect of link list
            current_node=current_node.next
        current_node.next=new_node

    def display(self):
        print(self,'this is self')
        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")
obj=Linklists()
obj.insertEndList(30)
obj.insertEndList(40)
obj.insertEndList(50)
obj.insertEndList(60)
obj.display()
# why you donot gives only link list() because it doesnot know which object have to do .so need reference
# 2️⃣ When you create object without variable

# You can actually do this:

# Linklists().insertEndList(30)

# This works, but the object disappears immediately.

# Example:

# Linklists().insertEndList(30)
# Linklists().insertEndList(40)

# Problem:

# Each time a new linked list is created.

# So:

# Linklists() → new list
# Linklists() → another new list

# They are not the same list.

# So the values are not stored together.
# obj=Linklists()
# obj2=Linklists()
# print(f'{obj}:1st,{obj2}:2nd')
# while True:
    # value=(input("give a number or for break press q: "))
    # if value=='q':
    #     break
    # obj2.insertEndList(value)
# obj.display()
# obj2.display()

# print(Linklists.count)

# print(obj)

        



