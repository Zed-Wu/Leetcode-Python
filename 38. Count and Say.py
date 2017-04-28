class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        start = '1'
        for i in range(0,n - 1):
            tmp = ''
            num = 1
            value = start[0]
            for j in range(1,len(start)):
                if start[j] == value:
                   num = num + 1
                else:
                    tmp = tmp + str(num) + value
                    value = start[j]
                    num = 1
            tmp = tmp + str(num) + value
            start = tmp
        return start

if __name__ == "__main__":
    solution = Solution()
    re = solution.countAndSay(4)
    print re