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
        if(str[i] == ' '):
            return 0
        flag = 1
        if(str[i] == '+'):
            flag = 1
            i = i + 1
        elif(str[i] == '-'):
            flag = 0
            i = i + 1
        elif(not str[i].isdigit()):
            return 0
        if(i >= len(str)):
            return 0
        for j in range(i,len(str)):
            if(not str[j].isdigit()):
                break
        if(not str[j].isdigit()):
            j = j - 1
        if (i == j + 1):
            return 0
        str = str[i:j + 1]
        if(flag == 1):
            if(int(str) > 2147483647):
                return 2147483647
            return int(str)
        else:
            if(int(str) > 2147483648):
                return -2147483648
            return -int(str)

if __name__ == '__main__':
    solution = Solution()
    re = solution.myAtoi('     -123*')
    print re
