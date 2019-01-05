class Solution(object):
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
