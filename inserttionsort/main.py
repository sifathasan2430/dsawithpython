array=[34,45,55,12,30]
for i in range(1,len(array)):
    key=i+1
    j=i-1
    while j>=0 and key<array[j]:
        array[j+1]=array[j]
        j=j-1
    array[j+1]=key
print(array)

