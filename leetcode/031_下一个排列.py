#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#
# https://leetcode-cn.com/problems/next-permutation/description/
#
# algorithms
# Medium (28.95%)
# Total Accepted:    8.2K
# Total Submissions: 27.7K
# Testcase Example:  '[1,2,3]'
#
# 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
# 
# 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
# 
# 必须原地修改，只允许使用额外常数空间。
# 
# 以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
# 1,3,2 > 2,1,3
# 
# 逆序 遇到第一个可以交换的组合就是执行组合
class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = len(nums) - 2

        while left >= 0 and nums[left+1] <= nums[left]:
            left -= 1
        
        if left >= 0:
            mid = len(nums) - 1
            while mid >= 0 and nums[mid] <= nums[left]:
                mid -= 1
            nums[left], nums[mid] = nums[mid], nums[left]
        
        left, right = left+1, len(nums) - 1

        while left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


# if __name__ == "__main__":
#     test_data = [1,5,4,7,6,5,3,1]
#     test_data = [5,1,1]
#     Solution().nextPermutation(test_data)
#     print(test_data)

