#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
# https://leetcode-cn.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (31.38%)
# Total Accepted:    47.4K
# Total Submissions: 150.4K
# Testcase Example:  '["flower","flow","flight"]'
#
# 编写一个函数来查找字符串数组中的最长公共前缀。
# 
# 如果不存在公共前缀，返回空字符串 ""。
# 
# 示例 1:
# 
# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 
# 
# 示例 2:
# 
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
# 
# 
# 说明:
# 
# 所有输入只包含小写字母 a-z 。
# 
#
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 1:
            return strs[0]
        elif len(strs) <= 0:
            return ''

        tree = Node()
        for item in strs:
            if not item:
                return '' 
            tree.add(item)
        
        return tree.same()
        

class Node:
    def __init__(self):
        self.root = {}
        self.word_end = -1
    
    def add(self, word):
        cur_node = self.root
        for c in word:
            if c not in cur_node:
                cur_node[c] = {}
            cur_node = cur_node[c]
        cur_node[self.word_end] = True
        
    def same(self):
        same_node = self.root
        result = ''
        while same_node:
            if len(same_node) == 1:
                key = list(same_node.keys())[0]
                if key == -1:
                    break
                result += key
                same_node = same_node[key]
            else:
                break
        
        return result


