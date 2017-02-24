class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        begin = 0
        end = 0
        re = [[0 for i in range(l)] for i in range(l)]
        for i in range(l):
            re[i][i] = 1
        for ltmp in range(2,l + 1):
            for i in range(l):
                if(ltmp + i <= l):
                    offset = 1
                    if(ltmp == 2):
                        offset = 0
                    if(re[i + offset][ltmp + i - 2] == 1 and s[i] == s[ltmp + i - 1]):
                        re[i][ltmp + i - 1] = 1
                        begin = i
                        end = ltmp + i - 1
        str_re = s[begin:end + 1]
        print str_re
        return str_re

if __name__ == '__main__':
    solution = Solution()
    solution.longestPalindrome("sb")
