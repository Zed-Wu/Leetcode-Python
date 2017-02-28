class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        re = 0
        while(i < j):
            tmp = min(height[i],height[j]) * (j - i)
            if tmp > re:
                re = tmp
            if(height[i] < height[j]):
                i = i + 1
            else:
                j = j - 1
        return re

if __name__ == '__main__':
    solution = Solution()
    re = solution.maxArea([3,1,2,3])
    print re