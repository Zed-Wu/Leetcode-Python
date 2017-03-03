class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        re = []
        nums.sort()
        last_i = nums[0] + 1
        for i in range(0,len(nums)):
            if nums[i] == last_i:
                continue
            last_i = nums[i]
            if i + 1 < len(nums):
                last_j = nums[i + 1] + 1
            for j in range(i + 1,len(nums)):
                if nums[j] == last_j:
                    continue
                last_j = nums[j]
                k = j + 1
                l = len(nums) - 1
                while k < l:
                    sum = nums[i] + nums[j] + nums[k] + nums[l]
                    if sum > target:
                        l = l - 1
                    elif sum < target:
                        k = k + 1
                    else:
                        tmp = []
                        tmp.append(nums[i])
                        tmp.append(nums[j])
                        tmp.append(nums[k])
                        tmp.append(nums[l])
                        re.append(tmp)
                        t = nums[k]
                        k = k + 1
                        while k < len(nums) and nums[k] == t:
                            k = k + 1
        return  re


if __name__ == '__main__':
    solution = Solution()
    re = solution.fourSum([1,0,-1,0,-2,2],0)
    print re