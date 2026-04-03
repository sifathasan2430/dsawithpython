class Node:
    def __init__(self,value):
        self.left=None
        self.right=None
        self.value=value
    
def pre_order(root):
    if root!=None:
        print(root.value,end=",")
        pre_order(root.left)
       
        pre_order(root.right)
      
def in_order(root):
    if root!=None:
        
        in_order(root.left)
        print(root.value,end=",")
        in_order(root.right)
def post_order(root):
    if root!=None:
        
        post_order(root.left)
        
        post_order(root.right)
        print(root.value,end=",")

root=Node(1)
root.left=Node(3)
root.right=Node(5)
root.left.left=Node(2)
root.left.right=Node(4)
root.right.right=Node(5)
root.right.right=Node(8)
pre_order(root)
print('')
in_order(root)
print('')
post_order(root)
