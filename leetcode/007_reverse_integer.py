#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#
# https://leetcode-cn.com/problems/reverse-integer/description/
#
# algorithms
# Easy (31.07%)
# Total Accepted:    76.8K
# Total Submissions: 245.6K
# Testcase Example:  '123'
#
# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
# 
# 示例 1:
# 
# 输入: 123
# 输出: 321
# 
# 
# 示例 2:
# 
# 输入: -123
# 输出: -321
# 
# 
# 示例 3:
# 
# 输入: 120
# 输出: 21
# 
# 
# 注意:
# 
# 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
# 
#
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x_to_s = str(x)
        if x < 0:
            result_num = -int(x_to_s[1:][::-1])
        else:
            result_num = int(x_to_s[::-1])

        return 0 if result_num > 2**31 - 1 or result_num < -2**31 else result_num
        
