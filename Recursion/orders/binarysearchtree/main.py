class Node:
    def __init__(self,value):

        self.left=self.right=None
        self.data=value
def insert(root,value):
    if root is None:
        return Node(value)
    if root.data==value:
        return root
    if root.data>value:
        root.left=insert(root.left,value)
    else:
        root.right=insert(root.right,value)
    return root
root=insert(None,4)
print(root)
root=insert(root,2)
root=insert(root,1)
root=insert(root,5)
root=insert(root,3)
root=insert(root,4)
root=insert(root,6)

print(root)


def search(root,value):
   
    if root is None:
        print("their is no data in this tree")
        return 
        
    if root.data==value:
        print("data found in the tree")
        return
        
    if root.data>value:
        search(root.left,value)
    else:
       search(root.right,value)
    
    return root
    
search_fn=search(root,9)
print(search_fn)
