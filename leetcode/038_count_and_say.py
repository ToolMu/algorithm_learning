#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 报数
#
# https://leetcode-cn.com/problems/count-and-say/description/
#
# algorithms
# Easy (47.39%)
# Total Accepted:    19.8K
# Total Submissions: 41.5K
# Testcase Example:  '1'
#
# 报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：
# 
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 
# 
# 1 被读作  "one 1"  ("一个一") , 即 11。
# 11 被读作 "two 1s" ("两个一"）, 即 21。
# 21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。
# 
# 给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。
# 
# 注意：整数顺序将表示为一个字符串。
# 
# 
# 
# 示例 1:
# 
# 输入: 1
# 输出: "1"
# 
# 
# 示例 2:
# 
# 输入: 4
# 输出: "1211"
# 
# 
#
class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for _ in range(1, n):
            s = self.count(s)
            
        return s

    def count(self, s):
        x = ''
        old_item = None
        count_num = 0
        for item in s:
            if (old_item and item==old_item) or old_item is None:
                count_num += 1
                old_item = item 
            elif old_item and item != old_item:
                x = x + str(count_num) + old_item
                count_num = 1
                old_item = item
            else:
                x = x + str(count_num) + item
                count_num = 0

        if count_num != 0:
            x = x + str(count_num) + old_item
        
        return x

