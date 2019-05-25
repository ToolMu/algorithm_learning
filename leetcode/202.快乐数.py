#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#
class Solution:
    def isHappy(self, n: int) -> bool:
        values = set()
        while n != 1:
            new_now = 0
            
            while n != 0:
                new_now += (n%10)**2
                n //= 10

            if new_now in values:
                return False
            else:
                values.add(new_now)
                n = new_now
        
        return True

