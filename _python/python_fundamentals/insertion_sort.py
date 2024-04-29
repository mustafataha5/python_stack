

def insertion_sort(arr,n):
    for i in range(1,n): 
        temp = arr[i]
        j= i-1 

        while(j>=0 and temp < arr[j]):
            arr[j+1] = arr[j]
            j =j-1 
        arr[j+1] = temp    

    return arr






arr=[8,5,1,3,2,4]
print(f"  insertion_sort({arr}) -->> ",insertion_sort(arr,len(arr)))
