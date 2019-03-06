# 构建大顶堆 每次堆顶和最后交换 并重建除了最后一个值以外的所有数所在的堆结构

def heap_sort(sorting_list):
    build_heap(sorting_list)
    for i in range(len(sorting_list)-1, 0, -1):
        sorting_list[i], sorting_list[0] = sorting_list[0], sorting_list[i] 
        adjust_heap(sorting_list, 0, i-1)
    
    return sorting_list


def build_heap(data):
    for i in range(len(data)//2, -1, -1):
        adjust_heap(data, i, len(data)-1)


def adjust_heap(heap_, start, end):
    root = start
    while root*2+1 <= end:
        child = root*2+1  # 叶的左节点
        if child+1 <= end and heap_[child] < heap_[child+1]:
            child += 1  # 校验叶的右节点是否存在并比左节点大
        
        if child <= end and heap_[root] < heap_[child]:  # 叶节点值大于根节点 交换
            heap_[root], heap_[child] = heap_[child], heap_[root]
            root = child
        else:
            return

    
if __name__ == "__main__":
    test_data = [4, 5, 2, 1, 8]
    print(heap_sort(test_data))
