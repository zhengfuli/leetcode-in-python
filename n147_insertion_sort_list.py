# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_head = ListNode(0)
        new_head.next = cur = head

        while cur and cur.next:
            dummy = new_head

            while cur.next and cur.next.val > dummy.next.val:
                if cur.next.val >= cur.val:
                    cur = cur.next
                else:
                    dummy = dummy.next

                if not cur.next: return new_head.next

            temp = cur.next
            cur.next = cur.next.next
            temp.next = dummy.next
            dummy.next = temp

        return new_head.next