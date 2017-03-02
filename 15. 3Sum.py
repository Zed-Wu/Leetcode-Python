class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        nums.sort()
        #print nums
        re = []
        d = dict()
        for i in range(0,len(nums)):
            if d.has_key(nums[i]):
                d[nums[i]] = d[nums[i]] + 1
            else:
                d[nums[i]] = 1

        #print d
        last_i = nums[0] + 1
        for i in range(0,len(nums) - 1):
            if nums[i] == last_i:
                continue
            last_i = nums[i]
            last_j = nums[i + 1] + 1
            for j in range(i + 1,len(nums)):
                if nums[j] == last_j:
                    continue
                last_j = nums[j]
                k = 0 - nums[i] - nums[j]
                d[nums[i]] = d[nums[i]] - 1
                d[nums[j]] = d[nums[j]] - 1
                tmp = []
                if d.has_key(k) and d[k] > 0:
                    #print i,j,k
                    tmp.append(nums[i])
                    tmp.append(nums[j])
                    tmp.append(k)
                    re.append(tmp)
                d[nums[i]] = d[nums[i]] + 1
                d[nums[j]] = d[nums[j]] + 1
        #print re
        return re

if __name__ == '__main__':
    solution = Solution()
    re = solution.threeSum([0,0,0])
    print re