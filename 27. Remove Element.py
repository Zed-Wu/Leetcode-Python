class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        indexOfnum = 0
        l = len(nums)
        for i in range(0,len(nums)):
            if nums[i] == val:
                l = l - 1
                continue
            nums[indexOfnum] = nums[i]
            indexOfnum = indexOfnum + 1
        return l,nums

if __name__ == "__main__":
    solution = Solution()
    re,nums = solution.removeElement([3,2,2,3],3)
    print re,nums