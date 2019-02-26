#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#
# https://leetcode-cn.com/problems/length-of-last-word/description/
#
# algorithms
# Easy (28.27%)
# Total Accepted:    16.2K
# Total Submissions: 56.7K
# Testcase Example:  '"Hello World"'
#
# 给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。
# 
# 如果不存在最后一个单词，请返回 0 。
# 
# 说明：一个单词是指由字母组成，但不包含任何空格的字符串。
# 
# 示例:
# 
# 输入: "Hello World"
# 输出: 5
# 
# 
# 双指针？？？
"""
def lengthOfLastWord(self, s):
    ls = len(s)
    # slow and fast pointers
    slow = -1
    # iterate over trailing spaces
    while slow >= -ls and s[slow] == ' ':
        slow-=1
    fast = slow
    # iterate over last word
    while fast >= -ls and s[fast] != ' ':
        fast-=1
    return slow - fast
"""
class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        for index, item in enumerate(s[::-1]):
            if item == ' ' and index != 0:
                return index
        
        return len(s) 

        
