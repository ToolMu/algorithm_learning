class Solution1(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        str_x = str(x)
        rstr_x = str_x[::-1]
        if str_x == rstr_x:
            return True

        return False


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):  # 条件2为了避免10这个例子
            return False

        reverse_num = 0
        while x > reverse_num:
            reverse_num = reverse_num * 10 + x % 10
            x = x // 10  # Py3除法的坑

        return x == reverse_num or x == reverse_num // 10


if __name__ == "__main__":
    solution = Solution()
    print(solution.isPalindrome(11))