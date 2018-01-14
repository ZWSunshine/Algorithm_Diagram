#递归实现列表中包含元素的个数

def count(arr):
    if len(arr) == 0:
        return 0
    return 1 + len(arr[1:])

list = [1,1,2,2,3,4,3,4,5,6,2]
print(count(list))
