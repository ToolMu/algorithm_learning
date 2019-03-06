def bubble_sort(sorting_list):
    count  = len(sorting_list)
    for i in range(count):  # 找一个位置
        for j in range(i+1, count):  # 从当前位置冒出
            if sorting_list[i] > sorting_list[j]:
                sorting_list[i], sorting_list[j] = sorting_list[j], sorting_list[i]
    
    return sorting_list


if __name__ == "__main__":
    test_data = [3,4,9,7,1]
    print(bubble_sort(test_data))
