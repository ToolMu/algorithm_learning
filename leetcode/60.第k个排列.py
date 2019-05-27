#
# @lc app=leetcode.cn id=60 lang=python3
#
# [60] 第k个排列
#
class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        result, k, fact = "", k - 1, 1
        for idx in range(1, n):
            fact *= idx
        
        perm = [i for i in range(1, n + 1)]

        for idx in range(n-1, -1, -1):
            curr = perm[int(k//fact)]
            result += str(curr)
            perm.remove(curr)
            if idx > 0:
                k %= fact
                fact /= idx

        return result

