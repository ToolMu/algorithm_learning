# 注意这里的中间值取法 -> 用的是最为简单的中间位
# 考虑前中后三个值中取中间值 OR 其它...

def quick_sort(sorting_list):
    if len(sorting_list) <= 1:  # 递归终结条件
        return sorting_list

    mid_num = sorting_list[len(sorting_list) // 2]  # 取中间值

    left = [item for item in sorting_list if item < mid_num]  # 收集小于中间值部分
    middle = [item for item in sorting_list if item == mid_num]  # 收集等于中间值部分
    right = [item for item in sorting_list if item > mid_num]  # 收集大于中间值部分

    return quick_sort(left) + middle + quick_sort(right)  # 小于和大于部分递归操作


if __name__ == "__main__":
    test_data = [4,2,6,7,1,9]
    print(quick_sort(test_data))
