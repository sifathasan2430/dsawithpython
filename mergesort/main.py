# def divider(array,l,r):
#     if l<r:
#         m=(l+r)//2
#         print(f"Dividing: {array[l:r+1]} | Indices: l={l}, m={m}, r={r}")
#         divider(array,l,m-1)
#         divider(array,m,r)
        
# array=[0,1,2,3,4,5,6,7]
# divider(array,array[0],(len(array)-1))

def divider(array, l, r, depth=0):
    indent = "  " * depth
    if l < r:
        m = (l + r) // 2
        print(f"{indent}├─ Dividing: {array[l:r+1]} | l={l}, m={m}, r={r}")
        
        divider(array, l, m, depth + 1)
        divider(array, m + 1, r, depth + 1)
    else:
        print(f"{indent}└─ Base case: [{array[l]}] at index {l}")

array = [14,12,76,48,22,15,10]
print(f"Array: {array}\n")
divider(array, 0, len(array) - 1)

def two_sort_merge(array1,array2):
    new_array=[]
    
    i=j=0
    while i<(len(array1)-1) and j<(len(array2)-1):
        if i>j:
            new_array.append(j)
            j=j+1
        else:
            new_array.append(i)
            i=i+1
    return new_array
fn=two_sort_merge([2,4,6,8],[1,5,9,10])
print(fn)