# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head: return

        slow = ListNode(0)
        fast = ListNode(0)
        slow.next, fast.next = head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        half_head = slow
        dummy = half_head.next

        while dummy.next:
            print(dummy.val)
            temp = dummy.next
            dummy.next = temp.next
            temp.next = half_head.next
            half_head.next = temp

        dummy = head
        while dummy and dummy.next:
            temp = half_head.next
            half_head.next = temp.next
            temp.next = dummy.next
            dummy.next = temp
            dummy = dummy.next.next