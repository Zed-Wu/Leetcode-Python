# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = []
        y = 0
        while(l1 != None and l2 != None):
            val = l1.val + l2.val + y
            l1 = l1.next
            l2 = l2.next
            x = val % 10
            y = int(val / 10)
            result.append(x)
        while (l1 != None):
            val = l1.val + y
            l1 = l1.next
            x = val % 10
            y = int(val / 10)
            result.append(x)
        while (l2 != None):
            val = l2.val + y
            l2 = l2.next
            x = val % 10
            y = int(val / 10)
            result.append(x)
        if(y == 1):
            result.append(y)
        return result

#if __name__ =='__main__':
#   solution=Solution()
