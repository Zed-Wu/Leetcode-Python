# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
'''
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        num = 0
        tmp = head
        while tmp != None:
            num = num + 1
            tmp = tmp.next
        n = num - n
        present = head
        if n == 0:
            if num == 1:
                return []
            return head.next
        for i in range(0,n):
            last = present
            present = present.next
            fol = present.next
        last.next = fol
        del present
        return head
'''

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if n == 0:
            return []
        p1 = head
        p2 = head
        for i in range(0,n - 1):
            p1 = p1.next
        if p1.next == None:
            return head.next
        while p1.next != None:
            last = p2
            p2 = p2.next
            p1 = p1.next
        last.next = p2.next
        return head

if __name__ == '__main__':
    solution = Solution()
    t = ListNode(1)
    t2 = ListNode(2)
    t.next = t2
    re = solution.removeNthFromEnd(t,1)
    print re