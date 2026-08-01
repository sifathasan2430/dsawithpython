price=[28,21,12,10]
weight=[7,3,4,5]
def merge(items,l,r,m):
    L=items[l:m+1]
    R=items[m+1:r+1]
    # print(f"left:{L} ,right:{R}")

    i=j=0
    k=l
    # print(L[i][len(L[i])-1],R[j][len(L[j])-1],'this is value')
    while i<len(L)and j<len(R):
        if L[i][len(L[i])-1]<R[j][len(L[j])-1]:
            items[k]=R[j]
            j=j+1 
            k=k+1
        else:
            # new_sorted_array.append(L[i])
            items[k]=L[i]
            i=i+1
            k=k+1
    while i<len(L):
        # new_sorted_array.append(L[i])
    
        items[k]=L[i]
        i=i+1
        k=k+1
    while j<len(R):
        items[k]=R[j]
        # new_sorted_array.append(R[j])
        j=j+1
        k=k+1
    
    

def divided(items,l,r):
    if l<r:
       m=(l+r)//2
       divided(items,l,m)
       divided(items,m+1,r)
       merge(items,l,r,m)


def fractional_knapsack(prices,weights,capacity):
    lenght=len(prices)
    price_per_weight=[(prices[i],weights[i],prices[i]/weights[i]) for i in range(0,lenght)]
    divided(price_per_weight,0,len(price_per_weight)-1)
    profit=0
    c=capacity
    i=0
    while c>0 and i<len(price_per_weight):
        print(c)
        if c>=price_per_weight[i][1]:
            
            c=c-price_per_weight[i][1]
            profit=profit+price_per_weight[i][0]
            
        else:
            i=i+1
        if c>0 and i<len(price_per_weight):
             profit=profit+(c/price_per_weight[i][1])*price_per_weight[i][1]
    print(f"Profit{profit}")

    
    
fn=fractional_knapsack(price,weight,20)

 