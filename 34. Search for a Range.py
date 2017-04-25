class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = 0
        end = len(nums)
        a = -1
        b = -1
        while start < end:
            mid = (start + end) / 2
            if nums[mid] >= target:
                if nums[mid] == target:
                    a = mid
                end = mid
            else:
                start = mid + 1

        start = 0
        end = len(nums)
        while start < end:
            mid = (start + end) / 2
            if nums[mid] > target:
                end = mid
            else:
                if nums[mid] == target:
                    b = mid
                start = mid + 1
        return [a,b]


if __name__ == "__main__":
    solution = Solution()
    re = solution.searchRange([],3)
    print re