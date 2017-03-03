class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return []
        nums.sort()
        d_value = 1000000
        for i in range(0,len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum = nums[j] + nums[k] + nums[i]
                if sum < target:
                    d = abs(sum - target)
                    if d_value > d:
                        re = sum
                        d_value = d
                    j = j + 1
                elif sum > target:
                    d = abs(sum - target)
                    if d_value > d:
                        re = sum
                        d_value = d
                    k = k - 1
                else:
                    return sum
        return re


if __name__ == '__main__':
    solution = Solution()
    re = solution.threeSumClosest([0,0,0],1)
    print re