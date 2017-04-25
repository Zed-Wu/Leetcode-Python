class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        ans = dict()
        for i in range(0,len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if len(stack) > 0:
                    ans[stack[-1]] = i
                    stack.pop()
        length = 0
        result = 0
        end = -2
        ans_list = sorted(ans.items(),key=lambda item:item[0],reverse = False)

        for i in range(0,len(ans_list)):
            key = ans_list[i][0]
            if length > result:
                result = length
            if key == end + 1:
                end = ans[key]
                length = length + end - key + 1
            elif key < end:
                continue
            else:
                end = ans[key]
                length = end - key + 1
        if length > result:
            result = length
        return result

if __name__ == "__main__":
    solution = Solution()
    re = solution.longestValidParentheses(")()())()()(")
    print re