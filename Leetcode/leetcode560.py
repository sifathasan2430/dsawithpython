def maxSubarraySum( arr, k):
        # code here 
        window_sum=0
        maxs=float("-inf")
        for i in range(0,k):
            window_sum+=arr[i]
        maxs=max(window_sum,maxs)
        
        
        out_going=0
        in_comming=k
        print(in_comming)
        while len(arr)>in_comming:
            # print(out_going)
            out_going=out_going+1
            in_comming=in_comming+1
            # print(len(arr),in_comming)
            
            # window_sum+=-arr[out_going]+arr[in_comming]
            
            
            # out_going=out_going+1
            # in_comming=in_comming+1
            print(in_comming,out_going)
        # return maxs
lists=[100, 200 ,300 ,400,800,1200]
fn=maxSubarraySum(lists,2)
print(fn)