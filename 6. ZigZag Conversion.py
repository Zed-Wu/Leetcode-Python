class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        re = ""
        l = len(s)
        if(numRows == 1):
            return s
        for i in range(1,(l - 1)/ (2 * numRows - 2) + 2):
            if ((i - 1) * (2 * numRows - 2) < l):
                re = re + s[(i - 1) * (2 * numRows - 2)]
                #print i,re
        for i in range(2, numRows):
            for j in range(1, (l - 1) / (2 * numRows - 2) + 2):
                if (i - 1 + (j - 1) * (2 * numRows - 2) < l):
                    re = re + s[i - 1 + (j - 1) * (2 * numRows - 2)]
                    #print i,j,re
                if (i - 1 + 2 * (numRows - i) + (j - 1) * (2 * numRows - 2) < l):
                    re = re + s[i - 1 + 2 * (numRows - i) + (j - 1) * (2 * numRows - 2)]
                    #print i,j,re
        for i in range(1,(l - 1) / (2 * numRows - 2) + 2):
            if (numRows - 1 + (i - 1) * (2 * numRows - 2) < l):
                re = re + s[numRows - 1 + (i - 1) * (2 * numRows - 2)]
                #print i,re
        return re

if __name__ == '__main__':
    solution = Solution()
    re = solution.convert("a",1)
    print re