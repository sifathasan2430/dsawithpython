def sub_array_sum(lists,target):
    sum=0
    maxs=float("-inf")
    for i in range(0,len(lists)-(target-1)):
        array=lists[i:target+i]
        print(array)
        for num in array:
            sum=sum+num
            
        maxs=max(sum,maxs)
        sum=0
        
    print(maxs)
    # wrong    
# def sliding_window(lists,target):
#    window_sum=0
#    maxs=float("-inf")
#    for i in range(0,target):
#        window_sum=window_sum+lists[i]
# #    maxs=max(window_sum,maxs)
#    answer=window_sum


#    for i in range(1,target+1):
#        print(lists[i+target-1])
#        print(answer)
#     #    answer=answer-(lists[i])+(lists[i+target-1])
#        print(answer)
#     #    print(window_sum)
# #        maxs=max(answer,maxs)
# #    print(maxs)
            
    

lists=[2,9,31,-4,21,7]
# sliding_window(lists,3)
sub_array_sum(lists,4)