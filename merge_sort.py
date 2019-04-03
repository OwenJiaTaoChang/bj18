# 归并排序
def merge_sort(alist):
    n = len(alist)
    if n <= 1:
        return alist
    mid = n//2

    # left采用归并排序后有序的新的列表
    left_li = merge_sort(alist[:mid])

    # right采用归并排序后有序的新的列表
    right_li = merge_sort(alist[mid:])

    # 将两个有序的子序列合并为一个新的整体
    # merge(left,right)
    left_point, right_point = 0, 0
    result = []

    while left_point < len(left_li) and right_point < len(right_li):
        if left_li[left_point] <= right_li[right_point]:
            result.append(left_li[left_point])
            left_point += 1
        else:
            result.append(right_li[right_point])
            right_point += 1

    result += left_li[left_point:]
    result += right_li[right_point:]
    return result

if __name__ == "__main__":
    li = [54,26,93,17,77,31,44,55,20]
    print(li)
    sorted_li = merge_sort(li)
    print(li)
    print(sorted_li)