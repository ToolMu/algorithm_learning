def bubble_sort(sorting_list):
    count  = len(sorting_list)
    for i in range(count):  # 找一个位置
        for j in range(i+1, count):  # 从当前位置冒出
            if sorting_list[i] > sorting_list[j]:
                sorting_list[i], sorting_list[j] = sorting_list[j], sorting_list[i]
    
    return sorting_list


def improved_bubble_sort(_list):
    count  = len(_list)
    for i in range(count):  # 找一个位置
        stop = True
        for j in range(i+1, count):  # 从当前位置冒出
            if _list[i] > _list[j]:
                # 当出现变换时即认为当前排序没完成
                # 当没有出现变换时即可认为该部分排序已经基本完成
                stop = False
                sorting_list[i], sorting_list[j] = _list[j], _list[i]
        
        if stop:
            break
    
    return _list


if __name__ == "__main__":
    test_data = [3,4,9,7,1]
    print(bubble_sort(test_data))
