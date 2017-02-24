class Solution(object):
    def twoSum(self, nums, target):
        length = len(nums)
        for i in range(0,length):
            for j in range(i+1,length):
                if(nums[i] + nums[j] == target):
                    result = []
                    result.append(i)
                    result.append(j)
                    return result
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
