def bubbleSort(relist):
    # 冒泡排序
    n = len(relist)
    # 外层循环是循环次数
    for i in range(n):
        # 内层循环是下标
        for j in range(0,n-i-1):
            if relist[j] > relist[j+1]:
                relist[j+1], relist[j] = relist[j], relist[j+1]
    return relist

print(bubbleSort([1,5,2,6,9,3]))