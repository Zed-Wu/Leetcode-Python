class Solution(object):
    def getNum(self,char):
        charList = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        n = [1, 5, 10, 50, 100, 500, 1000]
        for i in range(0,7):
            if char == charList[i]:
                return n[i]

    def getIndex(self,char):
        charList = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        for i in range(0, 7):
            if char == charList[i]:
                return i

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        re = 0
        lastIndex = 10
        lastNum = 0
        for i in range(0,len(s)):
            re = re + self.getNum(s[i])
            i_index = self.getIndex(s[i])
            if i_index > lastIndex:
                re = re - 2 * lastNum
            lastIndex = i_index
            lastNum = self.getNum(s[i])
        return re

if __name__ == '__main__':
    solution = Solution()
    re = solution.romanToInt("X")
    print re