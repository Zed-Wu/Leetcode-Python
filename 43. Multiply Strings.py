class Solution(object):
    def strToint(self,num):
        re = 0
        for i in range(0,len(num)):
            re = re * 10
            re = re + int(num[i])
        return re

    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = self.strToint(num1)
        num2 = self.strToint(num2)
        num = num1 * num2
        return str(num)

if __name__ == "__main__":
    solution = Solution()
    re = solution.multiply("123","345")
    print re