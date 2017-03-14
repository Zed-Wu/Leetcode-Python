# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        if head.next == None:
            return head
        tmp = head.next
        head.next = tmp.next
        tmp.next = head
        last = head
        begin = head.next
        head = tmp
        if begin == None:
            return head
        while begin.next != None:
            tmp = begin.next
            begin.next = tmp.next
            tmp.next = begin
            last.next = tmp
            begin = begin.next
            last = tmp.next
            if begin == None:
                break
        return head

if __name__ == "__init__":
    solution = Solution()
    x1 = ListNode(1)
    x2 = ListNode(2)
    x3 = ListNode(3)
    x4 = ListNode(4)
    x1.next = x2
    x2.next = x3
    x3.next = x4
    print x1
    re = solution.swapPairs(x1)
    print re
