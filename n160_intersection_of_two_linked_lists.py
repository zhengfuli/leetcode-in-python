# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        dummyA, dummyB = headA, headB
        lenA, lenB = 0, 0

        while dummyA:
            lenA += 1
            dummyA = dummyA.next

        while dummyB:
            lenB += 1
            dummyB = dummyB.next

        (short, long) = (headA, headB) if lenA < lenB else (headB, headA)

        diff = abs(lenA - lenB)

        while diff:
            long = long.next
            diff -= 1

        while short and long:
            if short == long:
                return short
            else:
                short, long = short.next, long.next