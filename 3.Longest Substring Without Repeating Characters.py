import Queue

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sdict = dict()
        result = 0
        que = Queue.Queue()
        for char in s:
            que.put(char)
            while(sdict.has_key(char)):
                tmp = que.get()
                sdict.pop(tmp)

            sdict[char] = 1
            if(que.qsize() > result):
                result = que.qsize()
        return result

if __name__ =='__main__':
    solution = Solution()
    re = solution.lengthOfLongestSubstring("pwwkew")
    print re