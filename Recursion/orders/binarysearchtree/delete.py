def delete(root,value):
    if root is None:
        print("no data found")
        return root
    if root.value==value:
        if root.right==None:
            return root.left
        if root.left==None:
            return root.right
        
    return root
        
        