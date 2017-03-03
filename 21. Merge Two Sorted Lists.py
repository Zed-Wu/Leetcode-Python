# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None and l2 == None:
            return []
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        if l1.val > l2.val:
            pre = l2
            l2 = l2.next
        else:
            pre = l1
            l1 = l1.next
        head = pre
        while l1 != None and l2 != None:
            if l1.val > l2.val:
                pre.next = l2
                l2 = l2.next
            else:
                pre.next = l1
                l1 = l1.next
            pre = pre.next
        if l1 != None:
            pre.next = l1
        if l2 != None:
            pre.next = l2
        return head

if __name__ == '__main__':
    solution = Solution()
    t = ListNode(5)
    t1 = ListNode(1)
    t2 = ListNode(2)
    t3 = ListNode(4)
    t4 = ListNode(5)
    t1.next = t2
    t2.next = t3
    re = solution.mergeTwoLists(t,t1)
    print re