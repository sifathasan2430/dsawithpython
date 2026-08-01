# Knapsack greedy problem

def knapsack_greedy(prices,weights,capacity):
   n=len(prices)
   ratio_lists=[(prices[i],weights[i],prices[i]/weights[i])for i in range(0,n)]

   for i in range(0,n):
      for j in range(0,n-1-i):
          if ratio_lists[j][2]<ratio_lists[j+1][2]:
              ratio_lists[j],ratio_lists[j+1]=ratio_lists[j+1],ratio_lists[j]
#    price=0
#    j=0
   
#    while capacity>0 and j<len(ratio_lists):
#         if ratio_lists[j][1]<=capacity:
#            capacity=capacity-ratio_lists[j][1]
#            price=price+ratio_lists[j][0]
           
#            j=j+1
#         if capacity>0:
            
#             price=price+(ratio_lists[j][0]/ratio_lists[j][1])/capacity
            
#    print(f"price:{price}")
   total=0
   for price,weight,ratio in ratio_lists:
    #   if tuple the all value consider other wise error
        if capacity>0 and weight<=capacity:
             print(total,price)
             total=total+price
             print(f"total:{total},price:{price}")
             capacity=capacity-weight
        else:
            break
        if capacity>0:
            print(f"capacity:{capacity}")
            total=total+(price/weight)*capacity
   print(total)
      

price  = [10, 5, 15, 7, 6, 18, 3]
weight = [2, 3, 5, 7, 1, 4, 1]
capacity = 15
knapsack_greedy(price,weight,capacity)