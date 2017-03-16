import re

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        ans = re.search(needle,haystack)
        #m = re.match(r'(\w+) (\w+)(?P<sign>.*)', 'hello world!')
        #print m.groups()
        print ans.groups()
        if ans != None:
            return ans.start()
        else:
            return -1

if __name__ == "__main__":
    solution = Solution()
    re = solution.strStr('bbbbababc','ab')
    print re