# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head

        slow = ListNode(0)
        slow.next = fast = head

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        head1, head2 = head, slow.next

        slow.next = None

        temp1, temp2 = self.sortList(head1), self.sortList(head2)

        merged_head = ListNode(0)
        dummy = merged_head

        while temp1 and temp2:
            if temp1.val < temp2.val:
                dummy.next = temp1
                temp1 = temp1.next
                dummy = dummy.next
            else:
                dummy.next = temp2
                temp2 = temp2.next
                dummy = dummy.next

        if temp1: dummy.next = temp1
        if temp2: dummy.next = temp2

        return merged_head.next