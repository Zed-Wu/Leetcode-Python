class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        re = ""
        if len(strs) == 0:
            return ""
        if len(strs[0]) == 0:
            return ""
        index = 0
        flag = 0
        while True:
            for i in range(0,len(strs)):
                if index > len(strs[i]) - 1:
                    flag = 1
                    break
                if i == 0:
                    tmp = strs[i][index]
                if tmp != strs[i][index]:
                    flag = 1
                    break
            if flag == 1:
                break
            re = re + strs[0][index]
            index = index + 1
        return re

if __name__ == '__main__':
    solution = Solution()
    re = solution.longestCommonPrefix([])
    print re