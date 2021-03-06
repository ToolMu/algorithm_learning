#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#
# https://leetcode-cn.com/problems/powx-n/description/
#
# algorithms
# Medium (30.79%)
# Total Accepted:    11.7K
# Total Submissions: 37.4K
# Testcase Example:  '2.00000\n10'
#
# 实现 pow(x, n) ，即计算 x 的 n 次幂函数。
# 
# 示例 1:
# 
# 输入: 2.00000, 10
# 输出: 1024.00000
# 
# 
# 示例 2:
# 
# 输入: 2.10000, 3
# 输出: 9.26100
# 
# 
# 示例 3:
# 
# 输入: 2.00000, -2
# 输出: 0.25000
# 解释: 2-2 = 1/22 = 1/4 = 0.25
# 
# 说明:
# 
# 
# -100.0 < x < 100.0
# n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。
# 
# 
#
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:  # 特殊情况
            return 1.0
        
        if n < 0:   # 位置变化
            x = 1 / x
            n = -n
        
        if n % 2:   # 奇数时
            return x * self.myPow(x, n - 1)
        else:       # 偶数时  
            return self.myPow(x*x, n/2)

        

