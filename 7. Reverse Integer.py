__author__ = 'GongDa'
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        upperbound = 2147483647
        str_x = str(x)
        l = len(str_x)
        offset = 0
        if(str_x[0] == '-'):
            offset = 1
        re = "0"
        flag = 0
        for i in range(1,l + 1 - offset):
            index = l - i
            if(str_x[index] != '0' or flag == 1):
                re = re + str_x[index]
                flag = 1
        re_int = int(re)
        if(re_int < upperbound):
            if(str_x[0] == '-'):
                return -re_int
            else:
                return re_int
        else:
            return 0


if __name__ == '__main__':
    solution = Solution()
    re = solution.reverse(123)
    print re