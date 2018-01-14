#归并排序

def merge(left,right):
    '''
    最划分好的数组单元进行一一的归并排序
    :param left: 有序序列的左部分
    :param right: 有序序列的右部分
    :return: 新的排序序列
    '''
    new_list = []
    j = k = 0
    while j < len(left) and k < len(right):
        if left[j] < right[k]:
            new_list.append(left[j])
            j += 1
        else:
            new_list.append(right[k])
            k += 1

    if j == len(left):
        for i in right[k:]:
            new_list.append(i)
    else:
            for i in left[j:]:
                new_list.append(i)

    return new_list


def mergesort(lists):
    '''
    将数组进行划分知道划分到最小的数组单元（仅含一个元素）
    :param lists:一组数据
    :return: 返回对参数进行过排序的数据
    '''
    if len(lists) < 2:
        return lists
    middle = len(lists)//2
    left = mergesort(lists[:middle])
    right = mergesort(lists[middle:])
    return merge(left,right)

#如果执行运行则执行if语句的内容，若作为模块导入使用则不运行if语句的内容。
if __name__ == '__main__':
    list = [4, 7, 8, 3, 5, 9]
    print(mergesort(list))