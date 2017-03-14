#Definition for singly-linked list.
import Queue

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class HeapNode(object):
    def __init__(self,x,index):
        self.val = x
        self.index = index
    def __cmp__(self, other):
        return cmp(self.val,other.val)

class Solution(object):
    def getHeap(self,lists):
        q = Queue.PriorityQueue()
        for i in range(0,len(lists)):
            if lists[i] != None:
                q.put(HeapNode(lists[i].val,i))
        return q

    def getMin(self,lists,q):
        if q.empty():
            return q,lists,0
        node = q.get()
        min = node.val
        index = node.index
        if lists[index].next != None:
            lists[index] = lists[index].next
            q.put(HeapNode(lists[index].val,index))
        else:
            lists[index] = None
        return q,lists,min

    def checkLists(self,lists):
        if len(lists) == 0:
            return 0
        for i in range(0,len(lists)):
            if lists[i] != None:
                return 1
        return 0

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if self.checkLists(lists) == 0:
            return []
        head = ListNode(0)

        q = self.getHeap(lists)
        q,lists, min = self.getMin(lists,q)
        head.val = min
        lastnode = head
        while self.checkLists(lists) != 0:
            node = ListNode(0)
            q,lists,min = self.getMin(lists,q)
            node.val = min
            lastnode.next = node
            lastnode = node
        return head

if __name__ == "__main__":
    solution = Solution()
    x = []
    y = []
    z = ListNode(1)
    x.append(y)
    print x
    re = solution.mergeKLists(x)
    print re
