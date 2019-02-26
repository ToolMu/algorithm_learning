#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个有序数组的中位数
#
# https://leetcode-cn.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (32.83%)
# Total Accepted:    32K
# Total Submissions: 97.5K
# Testcase Example:  '[1,3]\n[2]'
#
# 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
# 
# 请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
# 
# 你可以假设 nums1 和 nums2 不会同时为空。
# 
# 示例 1:
# 
# nums1 = [1, 3]
# nums2 = [2]
# 
# 则中位数是 2.0
# 
# 
# 示例 2:
# 
# nums1 = [1, 2]
# nums2 = [3, 4]
# 
# 则中位数是 (2 + 3)/2 = 2.5
# 
# 
#
# 主要思路在于对K值的查找   这里的k值为中位数位置
# 对于nums1来说取n个数， 同时nums2则是要取k-n
# 
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len_s1, len_s2 = len(nums1), len(nums2)
        if len_s1 > len_s2:
            return self.findMedianSortedArrays(nums2, nums1)

        k_num = (len_s1 + len_s2 + 1) // 2 

        l_num, r_num = 0, len_s1

        while l_num <= r_num:
            n = (l_num+r_num) // 2
            m = k_num - n

            if n < r_num and nums1[n] < nums2[m-1]:
                l_num += 1
            elif n > 0 and nums1[n-1] > nums2[m]:
                r_num -= 1
            else:
                if n == 0:
                    l_max = nums2[m-1]
                elif m == 0:
                    l_max = nums1[n-1]
                else:
                    l_max = max(nums1[n-1], nums2[m-1])
        
                if (len_s1+len_s2) % 2:
                    return l_max
                
                if n == len_s1:
                    r_min = nums2[m]
                elif m == len_s2:
                    r_min = nums1[n]
                else:
                    r_min = min(nums1[n], nums2[m])

                return (l_max+r_min) * 0.5 

