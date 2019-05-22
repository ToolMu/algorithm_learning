#
# @lc app=leetcode.cn id=172 lang=python3
#
# [172] 阶乘后的零
#
class Solution:
    def trailingZeroes(self, n: int) -> int:
        zero_sum = 0
        
        while n > 0:
            n = int(n / 5)
            zero_sum += n

        return zero_sum
             
