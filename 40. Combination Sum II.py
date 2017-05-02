class Solution(object):
    def seeksolutino(self,candidates,target,index,numOfdict):
        result = []
        if len(candidates) <= index:
            return result
        #cur_value = candidates[0]
        cur_value = candidates[index]
        max = target / cur_value
        if max > numOfdict[candidates[index]]:
            max = numOfdict[candidates[index]]
        #can_tmp = copy.deepcopy(candidates)
        #del(can_tmp[0])

        for i in range(0,max + 1):
            re_tmp = []
            for j in range(0, i):
                re_tmp.append(cur_value)
            if target == i * cur_value:
                if re_tmp not in result:
                    result.append(re_tmp)
                return result
            next_tar = target - i * cur_value
            re = self.seeksolutino(candidates,next_tar,index + 1,numOfdict)
            for j in range(0,len(re)):
                re_tmp.extend(re[j])
                re_tmp.sort()
                if re_tmp not in result:
                    result.append(re_tmp)
                re_tmp = []
                for k in range(0, i):
                    re_tmp.append(cur_value)
        return result

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        numOfdict = dict()
        for i in range(0,len(candidates)):
            if numOfdict.has_key(candidates[i]):
                numOfdict[candidates[i]] = numOfdict[candidates[i]] + 1
            else:
                numOfdict[candidates[i]] = 1
        candidates = list(set(candidates))
        re = self.seeksolutino(candidates, target, 0, numOfdict)
        '''
        new_re = []
        for ele in re:
            if ele not in new_re:
                new_re.append(ele)
        '''
        return re

if __name__ == "__main__":
    solution = Solution()
    re = solution.combinationSum2([10,1,2,7,6,1,5],8)
    print re