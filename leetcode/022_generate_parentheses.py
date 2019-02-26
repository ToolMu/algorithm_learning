#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#
# https://leetcode-cn.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (67.51%)
# Total Accepted:    13.5K
# Total Submissions: 20K
# Testcase Example:  '3'
#
# 给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
# 
# 例如，给出 n = 3，生成结果为：
# 
# [
# ⁠ "((()))",
# ⁠ "(()())",
# ⁠ "(())()",
# ⁠ "()(())",
# ⁠ "()()()"
# ]
# 
# 
#
class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res_data = []
        def mor(left, right, one):
            if len(one) == 2*n:
                res_data.append(one)
                return 

            if left < n:
                mor(left+1, right, one+'(')
            if left > right:
                mor(left, right+1, one+')')

        mor(0, 0, '')
        return res_data            

        
