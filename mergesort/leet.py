class Solution(object):
    def twoSum(self, nums, target):
        def merge(array,l,r,m):
    
            L=array[l:m+1]
            R=array[m+1:r+1]

    
            
    
    ``i=j=0
    k=l
    
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
        
        
        divider(array,l,m)
        divider(array,m+1,r)
        merge(array,l,r,m)
        
        left=0
        right=len(nums)-1
        while left<right:
            if nums[left]+nums[right]==target:
                return [left,right]
            elif nums[left]+nums[right]>=target:
                right=right-1
            else:
                left=left+1
        
                    
    
        