#快速排序的算法递归实现

def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i < pivot]
        bigger = [i for i in arr[1:] if i > pivot]
        return quicksort(less)+[pivot]+quicksort(bigger)

list = [6,2,8,4,3,1,7,5]
print(quicksort(list))