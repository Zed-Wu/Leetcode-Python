class Solution(object):
    def search(self, nums, target):
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
            elif nums[mid] < target:
                if nums[mid] < nums[start]:
                    if target < nums[start]:
                        start = mid + 1
                    else:
                        end = mid
                else:
                    start = mid + 1
            else:
                if nums[mid] < nums[start]:
                    end = mid
                else:
                    if target < nums[start]:
                        start = mid + 1
                    else:
                        end = mid
        return -1


if __name__ == "__main__":
    solution = Solution()
    re = solution.search([1],1)
    print re