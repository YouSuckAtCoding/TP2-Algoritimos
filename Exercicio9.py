def quicksort(arr): #Utilizei o mesmo método de quick sort que usei no execício 2
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)

print(quicksort([9,5,8,7,1,6,4,2,33,55,77,44,11,5,4,12]));