class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        nums.sort()
        re = []
        last = nums[0] + 1
        for i in range(0,len(nums)):
            if nums[i] == last:
                continue
            last = nums[i]
            j = i + 1
            k = len(nums) - 1
            while j < k:
                n = nums[i]
                sum = nums[j] + nums[k]
                if sum > -n:
                    k = k - 1
                elif sum < -n:
                    j = j + 1
                else:
                    tmp = []
                    tmp.append(nums[i])
                    tmp.append(nums[j])
                    tmp.append(nums[k])
                    re.append(tmp)
                    t= nums[j]
                    j = j + 1
                    while j < len(nums) and nums[j] == t:
                        j = j + 1

        return re

if __name__ == '__main__':
    solution = Solution()
    re = solution.threeSum([0,0,0])
    print re