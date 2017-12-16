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
        dummy1 = l1
        while dummy1.next:
            if dummy1.x <= l2.x:
                dummy1.next = l2
                l2 = l2.next
            dummy1 = dummy1.next
        return l1
        dummy, dummy1, dummy2 = ListNode(0), l1, l2
        new_head = dummy
        while dummy1 and dummy2:
            if dummy1.val <= dummy2.val:
                dummy.next = dummy1
                dummy1 = dummy1.next
            else:
                dummy.next = dummy2
                dummy2 = dummy2.next
            dummy = dummy.next
        while dummy1:
            dummy.next = dummy1
            dummy1 = dummy1.next
            dummy = dummy.next
        while dummy2:
            dummy.next = dummy2
            dummy2 = dummy2.next
            dummy = dummy.next
        return new_head.next