coins=[1, 5, 10, 20]
Amount = 37
counter=0
j=len(coins)-1

while Amount>0 :
     
        
        if j>=0 and Amount>=coins[j]:
                print(f"Amount:{Amount},coins{coins[j]}")
               
                counter=counter+1
                print(counter)
                Amount=Amount-coins[j]
                j=j-1
        elif j<0 and Amount!=0:
                
                j=len(coins)-1
        else:
                break
                
               
        
        
                
                
        
                
        
