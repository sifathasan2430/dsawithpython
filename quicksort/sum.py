def divided(array,l,r):
    print(l,r)
    if l==r:
        return array[l]
    if l<r:
        m=(l+r)//2
        left=divided(array,l,m)
        right=divided(array,m+1,r)
    if left>right:
        return left
    else:
        return right
    # merge(array,l,r,m)
# def merge(array,l,r,m):
#     L=array[l:m+1]
#     R=array[m+1,r+1]
#     new_array=[]
#     i=0
#     j=0
#     total=0
#     while l<len(L) and r<len(L):
#         total=L[i]+[j]
#         i=i+1
#         j=j+1
#     return total
#     print(total)
lists=[12,14,18,22]
fn=divided(lists,0,len(lists)-1)
print(fn)     
