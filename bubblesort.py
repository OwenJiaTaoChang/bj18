def bubbleSort(relist):
    # len_ = len(relist)
    for i in range(len(relist)):
        for j in range(0,len(relist)-i-1):
            if relist[j] > relist[j+1]:
                relist[j+1], relist[j] = relist[j], relist[j+1]
    return relist

print(bubbleSort([1,5,2,6,9,3]))