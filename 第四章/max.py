#求列表中的最大数

def max(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = max(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max

list = [3,1,5,2,6,2,83,98,235,1,4,2,6,2]
print(max(list))