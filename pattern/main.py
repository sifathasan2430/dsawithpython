def pattern(n):
    for i in range(0,n):
        for j in range(0,i+1):
            if (j+1)%2==0:
                print(1,end=" ")
            else:
                print(0,end=" ")
        print()
      
pattern(5)