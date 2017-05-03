class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        re = 0
        if len(height) == 0:
            return re
        l = 0
        r = len(height) - 1
        while l < r:
            if height[l] < height[r]:
                tmp = height[l]
                while tmp >= height[l]:
                    re = re + tmp - height[l]
                    l = l + 1
                    if l > r:
                        break
            else:
                tmp = height[r]
                while tmp >= height[r]:
                    re = re + tmp - height[r]
                    r = r - 1
                    if r < l:
                        break
        return re

if __name__ == "__main__":
    solution = Solution()
    re = solution.trap([5,5,1,7,1,1,5,2,7,6])
    print re