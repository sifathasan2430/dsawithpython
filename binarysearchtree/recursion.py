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
root=insert(root,6)
root=insert(root,5)
root=insert(root,2)

# root=insert(root,7)

root=insert(root,6)



root=insert(root,1)

root=insert(root,3)
def in_order(root):
    if root!=None:
        in_order(root.left)
        print(root.data,end=",")
        in_order(root.right)
    return
in_order(root)



def search(root,value):
    print(root.left)
    if root is None:
        
        print("data is not found")
        return root
    if root.data==value:
        print("result found in the tree",root.data)
        return root
    if root.data>value:
        print("hit")
        # root.left=search(root.left,value) for searching not insert
        return search(root.left,value)   # ✅ no assignment
    if root.data<value: 
        return search(root.right,value)
    
    return root

search(root,1)
print(root)
