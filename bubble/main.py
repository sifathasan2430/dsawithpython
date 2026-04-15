def bubble_sort(bubble_array):
    for i in range(len(bubble_array)):
        for j in range(len(bubble_array)-1-i):
                print(bubble_array)
                if bubble_array[j]>bubble_array[j+1]:
                   bubble_array[j],bubble_array[j+1]=bubble_array[j+1],bubble_array[j]
                print(f"after:{bubble_array}")
    return bubble_array
fn=bubble_sort([6,5,4,3,2,1])
print(fn)
