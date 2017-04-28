import copy

class Solution(object):
    def seeksolutino(self,candidates,target,index):
        result = []
        if len(candidates) <= index:
            return result
        #cur_value = candidates[0]
        cur_value = candidates[index]
        max = target / cur_value
        #can_tmp = copy.deepcopy(candidates)
        #del(can_tmp[0])

        for i in range(0,max + 1):
            re_tmp = []
            for j in range(0, i):
                re_tmp.append(cur_value)
            if target == i * cur_value:
                result.append(re_tmp)
                return result
            next_tar = target - i * cur_value
            re = self.seeksolutino(candidates,next_tar,index + 1)
            for j in range(0,len(re)):
                re_tmp.extend(re[j])
                result.append(re_tmp)
                re_tmp = []
                for k in range(0, i):
                    re_tmp.append(cur_value)
        return result

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        re = self.seeksolutino(candidates,target,0)
        return re

if __name__ == "__main__":
    solution = Solution()
    re = solution.combinationSum([44,40,27,30,23,36,49,22,43,24,28,34,45,26,38,41,39,47,32,35,33,42,20,37,21,25,48,46],67)
    print re