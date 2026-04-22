def quick_sort(array,l,r):
    pivot=array[l]
    print(array)
    i=l
    j=r
  
    while True:
        while  array[i]<pivot:
            i=i+1
        while array[j]>pivot:
            print("hit",j)
            j=j-1
        if i>=j:
            
            return j
        
        array[i],array[j]=array[j],array[i]
        i=i+1
        j=j-1

def divided(array,l,r):
    if l<r:
        p=quick_sort(array,l,r)
   
        
        divided(array,l,p)
        divided(array,p+1,r)
lists3=[4, 2, 6, 5, 3, 9]
divided(lists3,0,len(lists3)-1)
print(lists3)
