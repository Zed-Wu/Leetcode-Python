import sys

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        if divisor == 0:
            return sys.maxint
        if dividend == 0:
            return 0
        if dividend * divisor > 0:
            flag = 1
        else :
            flag = 0
        dividend = dividend.__abs__()
        divisor = divisor.__abs__()

        tmp = dividend
        result = 0
        while True:
            result_tmp = 1
            if tmp < divisor:
                if flag == 0:
                    result = -result
                if result > sys.maxint:
                    return sys.maxint
                return result
            cur_divisor = divisor
            while tmp >= cur_divisor:
                cur_divisor = cur_divisor << 1
                result_tmp = result_tmp << 1
            result_tmp = result_tmp >> 1
            result = result + result_tmp

            cur_divisor = cur_divisor >> 1
            tmp = tmp - cur_divisor

if __name__ == "__main__":
    solution = Solution()
    re = solution.divide(-2147483648,-1)
    print re