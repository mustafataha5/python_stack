


def selection_sort(arr): 
    for i in range(len(arr)):
        min = i
        for j in range(i,len(arr)):
            if arr[min] > arr[j] : 
                min = j 
        arr[min],arr[i] = arr[i],arr[min]
    return arr 

arr = [-3, 0 ,4,8,3,-2]
print("Before ",arr)
print("After ",selection_sort(arr))
            