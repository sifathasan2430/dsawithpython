class Node:
    def __init__(self,value):
        self.left=self.right=None
        self.value=value
def insertion(root,value):
    if root is None:
        return Node(value)
    elif root.value==value:
        return root
    elif root.value>value:
        root.left=insertion(root.left,value)
    else:
        root.right=insertion(root.right,value)
    return root

root=insertion(None,4)
root=insertion(root,6)
root=insertion(root,2)
root=insertion(root,3)
root=insertion(root,1)
root=insertion(root,5)
root=insertion(root,7)

def in_order(root):
    if root !=None:
        in_order(root.left)
        print(root.value,end=",")
        in_order(root.right)
# in_order(root)




def find_successor(root,value):
    if root is None:
        print("data not found")
    elif root.value==value:
        print("data present here")
        if root.right!=None:
            root=root.right
            while root.left !=None:
                root=root.left
            print(f"successor:{root.value}")
            return root.value
    elif root.value>value:
        return find_successor(root.left,value)
    else:
        return find_successor(root.right,value)
    return root
# find_successor(root,6)






def delete_tree(root,value):
    # print(root.value)
    if root is None:
        print("data is not found")
    return None   
    if root.value==value:
        if root.left is None:
            return root.right
        if  root.right is None:
            return root.left
        else:
            print("hit")
            succ=find_successor(root,value)
            print(f"successor{succ}")
          
            root.value=succ
            root.right=delete_tree(root.right,succ)
            return root
            
        


    if root.value>value:
        root.left= delete_tree(root.left,value)
    if root.value<value: 
        root.right= delete_tree(root.right,value)
    return root


data=int(input("Enter the node data: "))

delete_data=delete_tree(root,data)
print(delete_data.value)
in_order(root)

    