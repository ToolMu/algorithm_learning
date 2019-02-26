# 三向字符串快速排序
class Quick3String:

    def _char_at(self, s, d):
        return ord(s[d]) if d < len(s) else -1

    def sort(self, strs):
        self._sort(strs, 0, len(strs)-1, 0)  # 待排序数组 起始位 终止位 切分位

    def _sort(self, a, lo, hi, d):
        if hi <= lo:   # 异常情况
            return 
        
        lt, gt = lo, hi   # 保存起点和终点
        v = self._char_at(a[lo], d)  # 取得标记点
        i = lo + 1

        while i <= gt:   # 遍历 归类
            t = self._char_at(a[i], d)
            if t < v:
                a[lt], a[i] = a[i], a[lt]
                lt += 1
                i += 1
            elif t > v:
                a[i], a[gt] = a[gt], a[i]
                gt -= 1
            else:
                i += 1
            
        self._sort(a, lo, lt-1, d)

        if v >= 0:
            self._sort(a, lt, gt, d+1)
        
        self._sort(a, gt+1, hi, d)
    

if __name__ == "__main__":
    test_cases = [
        'edu.princeton.cs',
        'com.apple',
        'com.cnn',
        'com.adobe',
        'edu.princeton.cs',
        'com.google'
    ]
    Quick3String().sort(test_cases)
    print(test_cases)