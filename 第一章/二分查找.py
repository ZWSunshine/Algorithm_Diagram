#二分查找算法实现代码

def binary_search(list,item):
    '''
    :param list: 要查找的数据组
    :param item: 要在数据组中查找的某个数据
    :return: item的当前索引位置
    '''
    low = 0
    high = len(list)-1
    while low <= high:
        mid = ((low + high) // 2)+1
        guess = list[mid]
        if guess == item:
            return mid
        elif guess > mid:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [1,3,5,7,9,11,13,15,17,19]

print(binary_search(my_list,5))
