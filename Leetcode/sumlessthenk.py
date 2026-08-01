# arr=[1,2,3]
# l=0
# r=0

# sum=0
# counter=0
# while l<len(arr):
#    if len(arr)>r:
#       sum+=arr[r]
#       print(sum)
#       if k==sum:
#          counter+=1
         

#       r+=1
#    else:
#       l+=1
#       r=l 
#       sum=0
# print(counter)
# # time complexity is O(n2)
arr=[2,5,1,7,10]
k=14
l=0
r=0
maxs=0
sum=0
while len(arr)>l:
    sum+=arr[r]
    if k>sum:
       
       maxs=max(r-l+1,maxs)
       r+=1
    else:
        sum-=arr[l]
        l+=1
print(maxs)
