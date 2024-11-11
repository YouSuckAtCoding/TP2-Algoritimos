#O algoritimo implementadoé o quick osrt, utilizando List Comprehension. 
# https://www.geeksforgeeks.org/python-program-for-quicksort/

def quicksort(arr): #Complexidade O(n log n)
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)
