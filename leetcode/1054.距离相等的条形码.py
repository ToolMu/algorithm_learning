class Solution(object):
    def rearrangeBarcodes(self, barcodes):
        """
        :type barcodes: List[int]
        :rtype: List[int]
        """
        bucket = [0 for _ in range(10001)]
        # 桶收集
        for item in barcodes:
            bucket[item] += 1
        # 统计最大值
        max_time = 0
        max_index = 0
        for index, item in enumerate(bucket):
            if item > max_time:
                max_time = item
                max_index = index
        
        pos = 0
        idx = 0
        while pos < len(barcodes):
            if bucket[max_index] <= 0:
                break
            else:
                bucket[max_index] -= 1
                barcodes[pos] = max_index
                pos += 2
                
        while pos < len(barcodes):
            if bucket[idx] <= 0:
                idx += 1
                continue
            else:
                bucket[idx] -= 1
                barcodes[pos] = idx
                pos += 2
        
        pos = 1
        while pos < len(barcodes):
            if bucket[idx] <= 0:
                idx += 1
                continue
            else:
                bucket[idx] -= 1
                barcodes[pos] = idx
                pos += 2
                
        return barcodes
