class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == None:
            return 0
        ans = len(nums)
        index = 1
        for i in range(0,len(nums)):
            if i == 0:
                last = nums[i]
                continue
            if nums[i] == last:
                ans = ans - 1
            else:
                nums[index] = nums[i]
                index = index + 1
            last = nums[i]
        return ans,nums


if __name__ == "__main__":
    solution = Solution()
    re,nums = solution.removeDuplicates([1,1,2])
    print re,nums