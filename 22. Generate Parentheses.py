class Solution(object):
    re =[]
    def gen(self,left,right,n,str):
        if left == n:
            for i in range(0,right):
                str = str + ')'
            self.re.append(str)
            return
        if left == 0:
            str = str + '('
            self.gen(1,1,n,str)
        else:
            tmp1 = str + '('
            self.gen(left + 1, right + 1, n, tmp1)
            if right > 0:
                tmp2 = str + ')'
                self.gen(left,right - 1,n,tmp2)

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.re = []
        self.gen(0,0,n,'')
        return self.re

if __name__ == '__main__':
    solution = Solution()
    re = solution.generateParenthesis(3)
    print re