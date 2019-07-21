from __future__ import division


def binary_search(_list, left, right, target):
    if right < left:
        return False

    mid = (left + right) // 2
    
    if _list[mid] == target:
        return mid
    
    if _list[mid] > target:
        return binary_search(_list, left, mid-1, target)
    else:
        return binary_search(_list, mid+1, right, target)
    

def search(_list, target):
    """
    指数搜索，听起来很高大上（其实就是不知道这什么鬼）
    看过代码后才发现就是二分搜索的一种优化
    通过1->2->4->8量级的变化压缩需要二分的列表大小
    """
    if _list[0] == target:
        return 0
    
    # 压缩二分查找的索引空间
    i = 1
    while i < len(_list) and _list[i] <= target:
        i = i * 2
    
    return binary_search(_list, i//2, min(i, len(_list)), target)


if __name__ == "__main__":
    test_data = [1, 3, 5, 6, 8, 10, 17, 20, 30]
    print(search(test_data, 8))
