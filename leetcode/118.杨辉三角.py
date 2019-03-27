#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#
# https://leetcode-cn.com/problems/pascals-triangle/description/
#
# algorithms
# Easy (60.73%)
# Total Accepted:    18.9K
# Total Submissions: 31.1K
# Testcase Example:  '5'
#
# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
# 
# 
# 
# 在杨辉三角中，每个数是它左上方和右上方的数的和。
# 
# 示例:
# 
# 输入: 5
# 输出:
# [
# ⁠    [1],
# ⁠   [1,1],
# ⁠  [1,2,1],
# ⁠ [1,3,3,1],
# ⁠[1,4,6,4,1]
# ]
# 
#
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        
        for item in range(numRows):
            row = [None for _ in range(item+1)]
            row[0], row[-1] = 1, 1
            
            for more_num in range(1, len(row)-1):
                row[more_num] = result[item-1][more_num-1] + result[item-1][more_num]
                
            result.append(row)
            
        return result

