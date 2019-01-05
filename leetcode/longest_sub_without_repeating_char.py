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
