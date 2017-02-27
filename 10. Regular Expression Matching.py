import re

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        pattern = re.compile(p)
        match = pattern.match(s)
        if(match):
            if(match.group() != s):
                return False
            return True
        else:
            return False

if __name__ == '__main__':
    solution = Solution()
    re = solution.isMatch('aa','aa')
    print re