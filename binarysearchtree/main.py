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
root=insert(root,2)
root=insert(root,1)
root=insert(root,3)

root=insert(root,20)
root=insert(root,14)
root=insert(root,13)
root=insert(root,12)
root=insert(root,25)
# print(root)
def In_order(root):
    if root !=None:
        In_order(root.left)
        print(root.data,end=",")
        In_order(root.right)


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

def find_successor(root,value):
    if root is None:
        return "No value found"
    if root.data==value:
        print("data found")
        if root.right !=None:
            root=root.right
            while root.left !=None:
                root=root.left
            return root
    if root.data>value:
        return find_successor(root.left,value)
    if root.data<value:
        return find_successor(root.right,value)
    return root

In_order(root)
# search_fn=search(root,9)
# print(search_fn)
print(find_successor(root,4))

def find_and_delete(root,value):
    if root is None:
        print("data is not in the tree")

        return
    if root.data==value:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        else:
            successor=(find_successor(root,value))
            print(f"successor={successor.data,id(successor)}")
            root.data=successor.data
            root.right=find_and_delete(root.right,successor.data)
            return root
            
            # successor.left=root.left
            # successor.right=root.right
            # find_and_delete(root,successor.data)
            # root=successor
            # return root
# You are trying to swap the node objects themselves,
#  but you are calling the delete function on the root again.
#  This creates a circular mess.
#  Standard BST deletion doesn't usually swap the nodes; it swaps the values.

# The standard way:

# Find the successor (the smallest value in the right subtree).

# Copy the successor's data into the current node.

# Call the delete function on the right subtree to remove the now-duplicate successor node.
        
    if root.data>value:
        root.left=find_and_delete(root.left,value)
    if root.data<value:
        root.right=find_and_delete(root.right,value) 
    return root
root_after_delete=find_and_delete(root,3)
In_order(root)