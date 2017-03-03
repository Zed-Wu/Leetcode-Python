class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = ['0']
        for i in range(0,len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            elif s[i] == ')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif s[i] == '}':
                if stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            elif s[i] == ']':
                if stack[-1] == '[':
                    stack.pop()
                else:
                    return False
        if len(stack) == 1:
            return True
        return False

if __name__ == '__main__':
    solution = Solution()
    re = solution.isValid("]")
    print re