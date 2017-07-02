__author__ = 'GongDa'
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if(head == None or head.next == None):
            return head
        newhead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newhead


if __name__ == "__main__":
    solution = Solution()
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    a.next = b
    b.next = c
    re = solution.reverseList(a)
    print re.next.next.val

