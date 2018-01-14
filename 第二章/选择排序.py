#选择排序代码实现

def findSmallest(arr):
    '''
    :param arr: 一组数据
    :return: 最小数据的索引位置
    '''
    smallest = arr[0]
    smallest_index = 0
    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    '''
    :param arr: 一组数据
    :return: 从小到大排好顺序的数据
    '''
    newArr = []
    for i in range(len(arr)):
        smallest_index = findSmallest(arr)
        newArr.append(arr.pop(smallest_index))       #此处的pop方法是列表的一种方法
    return newArr

arr = [5,3,2,6,10]
print(selectionSort(arr))