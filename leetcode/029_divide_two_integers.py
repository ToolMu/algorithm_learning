#
# @lc app=leetcode.cn id=29 lang=python3
#
# [29] 两数相除
#
# https://leetcode-cn.com/problems/divide-two-integers/description/
#
# algorithms
# Medium (17.13%)
# Total Accepted:    7.9K
# Total Submissions: 45.7K
# Testcase Example:  '10\n3'
#
# 给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
# 
# 返回被除数 dividend 除以除数 divisor 得到的商。
# 
# 示例 1:
# 
# 输入: dividend = 10, divisor = 3
# 输出: 3
# 
# 示例 2:
# 
# 输入: dividend = 7, divisor = -3
# 输出: -2
# 
# 说明:
# 
# 
# 被除数和除数均为 32 位有符号整数。
# 除数不为 0。
# 假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。本题中，如果除法结果溢出，则返回 231 − 1。
# 
# 
#
class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        mark = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        
        time = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                time += i
                i <<= 1
                temp <<= 1
        
        time = time if mark else -time
        return min(max(-2147483648, time), 2147483647)

        
