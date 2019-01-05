class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x_to_s = str(x)
        if x < 0:
            result_num = -int(x_to_s[1:][::-1])
        else:
            result_num = int(x_to_s[::-1])

        return 0 if result_num > 2**31 - 1 or result_num < -2**31 else result_num


if __name__ == "__main__":
    solution = Solution()
    print(solution.reverse(123))
    print(solution.reverse(-111111119))
