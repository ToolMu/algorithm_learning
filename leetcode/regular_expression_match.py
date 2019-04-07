class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
            return not s

        if p[-1] == '*':
            if self.isMatch(s, p[:-2]):
                return True
            if s and (s[-1] == p[-2] or p[-2] == '.') and self.isMatch(
                    s[:-1], p):
                return True

        if s and (s[-1] == p[-1] or p[-1] == '.') and self.isMatch(
                s[:-1], p[:-1]):
            return True

        return False
