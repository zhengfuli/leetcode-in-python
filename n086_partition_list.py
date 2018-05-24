# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        smaller_head, larger_head = ListNode(0), ListNode(0)
        temp, dummy1, dummy2 = head, smaller_head, larger_head

        while temp:
            if temp.val < x:
                smaller_head.next = temp
                temp = temp.next
                smaller_head = smaller_head.next
                smaller_head.next = None
            else:
                larger_head.next = temp
                # changing temp here is very important, or the rest link list will be removed
                temp = temp.next
                larger_head = larger_head.next
                # cannot omit the following line, clip the rest part of temp
                larger_head.next = None

        smaller_head.next = dummy2.next
        return dummy1.next
