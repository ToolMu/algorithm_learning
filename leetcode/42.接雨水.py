#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#
# https://leetcode-cn.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (42.80%)
# Total Accepted:    11.2K
# Total Submissions: 26.1K
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
# 
# 
# 
# 上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢
# Marcos 贡献此图。
# 
# 示例:
# 
# 输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6
# 
#
# way 2: 栈方式 -> 栈底到栈顶应该是递减（只是说明）
class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        left_max = right_max = sum_water = 0
        while left <= right:
            # 总是固定一边的最大值移位
            if left_max <= right_max:
                left_max = max(left_max, height[left])
                sum_water += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                sum_water += right_max - height[right]
                right -= 1
        return sum_water
        

