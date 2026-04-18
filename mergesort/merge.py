def two_sort_merge(array1,array2):
    new_array=[]
    
    i=j=0
    while i<(len(array1)) and j<(len(array2)):
        if array1[i]>array2[j]:
            print(array2[j],end=',')
            # print(f"value:{array2[j]} index:{i}")
            j=j+1
        else:
            print(array1[i],end=",")
            # print(f"value:{array2[i]} index:{i}")
            i=i+1
    while j<(len(array2)):
            print(array2[j],end=',')
            j=j+1
    while i<(len(array1)):
            print(array1[i],end=',')
            i=i+1
    return new_array
fn=two_sort_merge([2,4,6,8],[1,5,9,10])
print(fn)