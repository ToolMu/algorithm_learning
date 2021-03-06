def interpolation_search(search_list, key):
    low, high = 0, len(search_list) - 1
    while low < high:
        mid = low+ int((high-low) * (key-search_list[low]) / (search_list[high]-search_list[low]))
        if key < search_list[mid]:
            high = mid - 1
        elif key > search_list[mid]:
            low = mid + 1
        else:
            return mid
    
    return -1


if __name__ == "__main__":
    test_data = [1, 3, 5, 6, 8, 10, 17, 20, 30]
    print(interpolation_search(test_data, 10))
