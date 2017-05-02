class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        for i in range(0,l):
            if i == nums[i] - 1:
                continue
            else:
                while nums[i] != i + 1:
                    if nums[i] > 0 and nums[i] - 1 < l:
                        tmp = nums[nums[i] - 1]
                        if tmp == nums[i]:
                            break
                        nums[nums[i] - 1] = nums[i]
                        nums[i] = tmp
                    else:
                        break
        for i in range(0,l):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1

if __name__ == "__main__":
    solution = Solution()
    re = solution.firstMissingPositive([2,2])
    print re