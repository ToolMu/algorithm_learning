# 预留前部作为已完成排序部分数据
# 每次新增数据插入合适位置

def insert_sort(sorting_list):
    for i in range(1, len(sorting_list)):
        swap_num = sorting_list[i]   # 定位一个临时交换值
        for j in range(i-1, -1, -1):  # 向以排序部分遍历合适位置 并插入
            if sorting_list[j] > swap_num:
                sorting_list[j], sorting_list[j+1] = sorting_list[j+1], sorting_list[j]
            else:
                sorting_list[j+1] = swap_num
                break
    
    return sorting_list


if __name__ == "__main__":
    test_data = [5, 3, 8, 1, 9]
    print(insert_sort(test_data))
