#
# @lc app=leetcode.cn id=223 lang=python3
#
# [223] 矩形面积
#
class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        area_num = (C-A)*(D-B) + (G-E)*(H-F)
        if E > C or F > D or G < A or H < B:
            return area_num
        
        I, J = max(A, E), max(B, F)
        K, L = min(C, G), min(D, H)
        return area_num - (K-I)*(L-J)



