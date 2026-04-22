def quick_sort(array,l):
    pivot=array[0]
    print(pivot)
    # this is wrong setting 0 and len(array)-1 hard coded
    i=0
    j=len(array)-1
    while True:
        while i>=(len(array)-1) and array[i]<pivot:
            i=i+1
        while j>=0 and array[j]>pivot:
            print("hit")
            j=j-1
        if i>=j:
            
            return j
        print(i,j,end=',')
        array[i],array[j]=array[j],array[i]
        i=i+1
        j=j-1

def divided(array,l,r):
    if l<r:
        p=quick_sort(array,l)
        
        divided(array,l,p)
        divided(array,p+1,r)
lists3=[4, 2, 6, 5, 3, 9]
divided(lists3,0,len(lists3)-1)
print(lists3,'this')
pivot=quick_sort(lists3,0)
print(pivot)