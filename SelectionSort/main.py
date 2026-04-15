array=[64,32]
# # min=array[0]
# for i in range(len(array)):
#     min=i
    
#     for j in range(i,len(array)-1):
#         if min>array[j+1]:
#             min=j+1
#     print(f"{array[i]}==={min}") 
#     print(array)       
    # array[i],min=min,array[i] 
#     # Expected Error
# If you use the Pythonic swap syntax array[i], 10 = 10, array[i], you will receive a SyntaxError: cannot assign to literal. 
# SitePoint
# SitePoint
# Why This Happens
# Target vs. Source: A swap requires two "targets" (variables or memory locations) to store data. A direct value (like 10) is a constant and does not have a memory address that can be reassigned.
# Assignment Logic: In a swap like a, b = b, a, the computer takes the value from b and puts it into the storage container a, then takes the value from a and puts it into b. You cannot "put" a value into a fixed number like 10.
# Index Errors: If you are trying to swap array[i] with a value at another index, and that index is larger than the list size, you will trigger an IndexError: list index out of range. 
# print(array,'final')

# # for i in range(len(array)):
# #     min=i
# #     for j in range(i,len(array)):
# #         # if min>j:wrong compare will be with value
# #         if array[min]>array[j+1]:
# #             min=j
# #     array[i],array[min]=array[min],array[i]
# # print(array)    
array=[64,42,50,63,34,30,32,25,27,20,23,15] 
for i in range(len(array)):
    min=i
    for j in range(i,len(array)):
        if array[min]>array[j]:
            min=j
    array[i],array[min]=array[min],array[i]
print(array)
        
