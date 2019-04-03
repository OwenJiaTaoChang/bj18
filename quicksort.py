def quicksort(alist):
    # 快速排序(重点掌握)
    if len(alist) < 2:
        return alist
    else:
        mid_value = alist[0]
        low = [i for i in alist[1:] if i <= mid_value]
        high = [j for j in alist[1:] if j > mid_value]
        return quicksort(low) + [mid_value] + quicksort(high)

print(quicksort([1,1,1,5,2,6,9,3]))