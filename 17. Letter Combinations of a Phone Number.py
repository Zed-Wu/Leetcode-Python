class Solution(object):
    re = []
    def Sea(self, ans, index, digits):
        if len(digits) == 0:
            return
        num2let = [[], ['a', 'b', 'c'], ['d', 'e', 'f'],\
                   ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'],\
                   ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z'],\
                   [' ']]
        if index == len(digits):
            self.re.append(ans)
            return
        num = int(digits[index]) - 1
        for i in range(0,len(num2let[num])):
            self.Sea(ans + num2let[num][i],index + 1,digits)

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        self.re = []
        self.Sea("",0,digits)
        return self.re

if __name__ == '__main__':
    solution = Solution()
    re = solution.letterCombinations("3")
    print re