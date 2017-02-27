class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x1 = str(x)
        offset = 0
        if(x1[0] == '-'):
            return  False
        for i in range(0 + offset,len(x1)):
            j = len(x1) -1 - i + offset
            if(x1[i] != x1[j]):
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    re = solution.isPalindrome(123321)
    print re