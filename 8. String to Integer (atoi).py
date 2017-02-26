__author__ = 'GongDa'
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if(len(str) == 0):
            return 0
        for i in range(0,len(str)):
            if(str[i] != ' '):
                break
        if((str[i] == '-' or str[i] == '+') and i == len(str) - 1):
            return 0
        if(str[i] != '-' and str[i] != '+' and (not str[i].isdigit())):
            return 0
        if(str[i] == '-' or str[i] == '+'):
            i = i + 1
        j = i + 1
        for j in range(i + 1,len(str)):
            if(not str[j].isdigit()):
                break
        str = str[i:j]
        print i,j
        if(int(str) > 2147483647):
            return 2147483647
        if(int(str) < -2147483648):
            return -2147483648
        return int(str)

if __name__ == '__main__':
    solution = Solution()
    re = solution.myAtoi('+1')
    print re
