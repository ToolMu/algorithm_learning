#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#
# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (27.49%)
# Total Accepted:    70.2K
# Total Submissions: 255.3K
# Testcase Example:  '"abcabcbb"'
#
# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
# 
# 示例 1:
# 
# 输入: "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 
# 
# 示例 2:
# 
# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 
# 
# 示例 3:
# 
# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
# 请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
# 
# 
#

# 双指针问题    简化版   处理记录的是指针的index位置信息
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len, begin_index = 0, 0
        char_map = {}

        for index, data in enumerate(s):
            if data in char_map.keys():
                begin_index = max(char_map[data], begin_index)

            max_len = max(max_len, index + 1 - begin_index)
            char_map[data] = index + 1

        return max_len
        


class Solution1(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        begin_index, end_index = 0, 0
        max_len = 0

        for data in s:
            if data in s[begin_index:end_index]:
                for str_i in s[begin_index:end_index]:
                    begin_index += 1
                    if str_i == data:
                        break

            end_index += 1

            if (end_index - begin_index) > max_len:
                max_len = end_index - begin_index

        return max_len


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len, begin_index = 0, 0
        char_map = {}

        for index, data in enumerate(s):
            if data in char_map.keys():
                begin_index = max(char_map[data], begin_index)

            max_len = max(max_len, index + 1 - begin_index)
            char_map[data] = index + 1

        return max_len


if __name__ == "__main__":
    test_group = [
        {
            "sub": "abcabcbb",
            "result": 3
        },
        {
            "sub": "bbbb",
            "result": 1
        },
        {
            "sub": "pwwkew",
            "result": 3
        },
    ]
    solution = Solution()
    for test_item in test_group:
        print("+ ---- +")
        print(test_item['result'])
        print(solution.lengthOfLongestSubstring(test_item['sub']))
