class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class ReverseKGroup(object):
    def reverse(self, start, end):
        # start is the node before the real starting one
        # end is the node after the last reversing one
        # return the node before end for the next reversing
        cur = start.next
        nex = cur.next
        while nex is not end:
            cur.next = nex.next
            nex.next = start.next
            start.next = nex
            nex = cur.next
        while start is not None:
            print start.val
            start = start.next
        return cur

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        new_head = start = ListNode(0)
        start.next = head
        end = head
        while True:
            for i in range(k):
                if end is None:
                    return new_head.next
                end = end.next
            start = self.reverse(start, end)
        return new_head.next