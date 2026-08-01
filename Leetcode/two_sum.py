def two_sum(lists,target):
  left=0
  right=len(lists)-1
  
  while left<right:
      if lists[left]+lists[right]==target:
         return [left,right]
      elif lists[left]+lists[right]>target:
         right=right-1
      else:
         left=left+1
nums = [2, 4, 7, 11, 15, 20]
target = 18
fn=two_sum(nums,target)
print(fn)
