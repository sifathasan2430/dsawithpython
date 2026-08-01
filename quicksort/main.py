def divider(array, l, r):
    # print(f'CALL → l:{l}, r:{r}')
    if l < r:
        m = (l + r) // 2
      
        divider(array, l, m)
        divider(array, m+1, r)
        merge(array,l,r,m)
       
def merge(array,l,r,m):
    L=array[l:m+1]
    R=array[m+1:r+1]
    print(f"left:{L}",end='|||')
    print(f'right:{R}')
    i=l,
    j=r
    k=l
    left_size=len(l)
    right_size=len(r)
    while i<left_size and L[i]<R[j]:
        array[k]=array[i]
    
    
    
lists=[12,16,14,22,13,24,30,10]
divider(lists,0,len(lists)-1)