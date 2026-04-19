def merge(array,l,r,m):
    # print(array[l:m+1],array[m+1:r+1])
    L=array[l:m+1]
    R=array[m+1:r+1]

    
    new_sorted_array=[]
    # i=j=k=0
    i=j=0
    k=l
    print(k)
    while i<len(L)and j<len(R):
        if L[i]>R[j]:
            array[k]=R[j]
            j=j+1 
            k=k+1
        else:
            # new_sorted_array.append(L[i])
            array[k]=L[i]
            i=i+1
            k=k+1
    while i<len(L):
        # new_sorted_array.append(L[i])
    
        array[k]=L[i]
        i=i+1
        k=k+1
    while j<len(R):
        array[k]=R[j]
        # new_sorted_array.append(R[j])
        j=j+1
        k=k+1
    
    

def divider(array,l,r):
    if l<r:
        m=(l+r)//2
        
        # print(array[l:r+1])
        divider(array,l,m)
        divider(array,m+1,r)
        merge(array,l,r,m)
        
        
        

lists=[12,14,34,45,23,4]
divider(lists,0,(len(lists)-1))
# print(lists)
