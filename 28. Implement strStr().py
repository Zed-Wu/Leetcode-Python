import re

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        ans = re.search(needle,haystack)
        if ans != None:
            return ans.start()
        else:
            return -1

if __name__ == "__main__":
    solution = Solution()
    re = solution.strStr('bbbbabcabc','ab')
    print re