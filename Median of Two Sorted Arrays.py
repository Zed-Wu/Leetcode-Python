class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        nums1.sort()
        print nums1
        if(len(nums1) % 2 == 1):
            re = nums1[len(nums1) / 2]
        else :
            print len(nums1)
            re = (float(nums1[len(nums1) / 2]) + float(nums1[len(nums1) / 2 - 1])) / 2
        return re

if __name__ == '__main__':
    solution = Solution()
    n1 = [1,2]
    n2 = [3,4]
    re = solution.findMedianSortedArrays(n1,n2)
    print re