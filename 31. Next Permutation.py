class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            return []
        ans_a = -1
        ans_b = -1
        a = 0
        b = 0
        for i in range(1,len(nums)):
            last = nums[a]
            cur = nums[i]
            if cur <= last:
                a = i
            elif cur > last:
                if cur > nums[b] and b > a:
                    a = b
                b = i
                ans_a = a
                ans_b = b
        if ans_a != -1:
            tmp = nums[ans_a]
            nums[ans_a] = nums[ans_b]
            nums[ans_b] = tmp
            tmp = nums[ans_a + 1:len(nums)]
            tmp.sort()
            nums[ans_a + 1:len(nums)] = tmp
        else:
            nums.reverse()
        return nums

if __name__ == "__main__":
    solution = Solution()
    re = solution.nextPermutation([2,1,3])
    print re