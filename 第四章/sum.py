#sum函数的代码

def sum(arr):
    '''
    :param arr: 一个列表
    :return: 列表所有元素的和
    '''
    if arr == []:
        return 0
    return arr[0] + sum(arr[1:])

list = [1,3,5,7,9]
print(sum(list))
