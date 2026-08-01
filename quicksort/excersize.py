def divider(array,l,r):
    if l<r:
        m=(l+r)//2
        divider(array,l,m)
        divider(array,m+1,r)
        print('left',array[l:m+1])
        print("right",array[m+1:r+1])
lists=[12,16,14,22,13,24,30,10]
divider(lists,0,len(lists)-1)