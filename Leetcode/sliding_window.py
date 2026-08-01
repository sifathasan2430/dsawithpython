def sliding_window(lists,target):
    window_sum=0
    maxs=float("-inf")
    for i in range(0,target):
        window_sum=window_sum+lists[i]
    maxs=max(window_sum,maxs)
    
    for j in range(1,len(lists)-target+1):
        print(window_sum,lists[j-1],lists[j+(target-1)])
        window_sum=window_sum-(lists[j-1])+lists[j+target-1]
        maxs=max(window_sum,maxs)
    print(maxs)
lists=[2,9,31,-4,21,7]
sliding_window(lists,3)