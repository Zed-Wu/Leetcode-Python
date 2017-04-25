class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums)
        while start < end:
            mid = (start + end) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid
            else:
                start = mid + 1
        return end


if __name__ == "__main__":
    solution = Solution()
    re = solution.searchInsert([1,2,3],0)
    print re