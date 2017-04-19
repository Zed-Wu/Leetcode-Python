import re

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        numOfword = len(words)
        str = words[0]
        l = len(str)
        le = l * numOfword
        word_dict = dict()
        result = []
        for i in range(0, numOfword):
            if word_dict.has_key(words[i]):
                word_dict[words[i]] = word_dict[words[i]] + 1
            else:
                word_dict[words[i]] = 1

        for left in range(0,len(s) - le + 1):
            word_use_dict = dict()
            right = left + le
            str = s[left:right]
            index = []
            flag = 0
            for i in range(0,numOfword):
                if word_use_dict.has_key(words[i]):
                    continue
                word_use_dict[words[i]] = 1
                pattern = re.compile(words[i])
                num = 0
                offset = 0
                for j in range(0,numOfword):
                    match = pattern.match(str,offset)
                    if match:
                        num = num + 1
                        index.append(match.start() + left)
                    offset = offset + l
                if num != word_dict[words[i]]:
                    flag = 1
                    break
            if flag != 1:
                index.sort()
                result.append(index[0])
        return result

if __name__ == "__main__":

    solution = Solution()
    res = solution.findSubstring("barfoothefoobarman", ["foo", "bar"])
    print res

