# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head

        cur, next = ListNode(0), head

        new_head = cur

        while next and next.next:
            if next.val == next.next.val:
                duplicate = next.val

                while next and next.val == duplicate:
                    next = next.next

            else:
                cur.next = next
                next = next.next
                cur = cur.next
                cur.next = None

        cur.next = next
        return new_head.next