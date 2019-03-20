def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [j for j in array[1:] if j > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([1,1,1,5,2,6,9,3]))