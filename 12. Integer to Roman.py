def cal(num,level,re):
    if(level < 0):
        return re
    char = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    n = [1, 5, 10, 50, 100, 500, 1000]
    th = [1, 4, 9, 40, 90, 400, 900]
    m = num / n[level]
    s = num % n[level]
    flag = 0
    for i in range(0, m):
        re = re + char[level]

    if s > th[level]:
        #print level
        for i in range(0,level):
            x = level - i - 1
            if x == 0 or x == 2 or x == 4:
                break
        s1 = n[x]
        s2 = s - n[level] + n[x]
        # s = m * n[level] - num
        tmp1 = cal(s1, level - 1, "")
        tmp2 = cal(s2, level, "")
        flag = 1
    elif s == th[level]:
        m = m + 1
        s = m * n[level] - num
        flag = 2
        tmp = cal(s, level - 1, "")
    else:
        tmp = cal(s, level - 1, "")

    if(flag == 1):
        re = re + tmp1 + char[level] + tmp2
    elif(flag == 2):
        re = re + tmp + char[level]
    else:
        re = re + tmp
    return re

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        re = cal(num,6,"")
        return re

if __name__ == '__main__':
    solution = Solution()
    re = solution.intToRoman(191)
    print re