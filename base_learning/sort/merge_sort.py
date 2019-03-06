def merge_sort(sorting_list):
    if len(sorting_list) <=1:  # 递归结束条件
        return sorting_list
    else:
        mid = len(sorting_list) // 2   # 二分
        left = merge_sort(sorting_list[:mid])  # 递归操作
        right = merge_sort(sorting_list[mid:])

        return merge(left, right)  # 合并递归操作
    
def merge(left, right):
    left_i, right_i = 0, 0
    result = []
    # 比对值
    while left_i < len(left) and right_i < len(right):
        if left[left_i] <= right[right_i]:
            result.append(left[left_i])
            left_i += 1
        else:
            result.append(right[right_i])
            right_i += 1
    
    # 添加未比对值
    result += left[left_i:]
    result += right[right_i:]

    return result


if __name__ == "__main__":
    test_data = [4, 3, 8, 10, 7]
    print(merge_sort(test_data))
