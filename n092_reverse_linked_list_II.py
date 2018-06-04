class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head

        pre_m = ListNode(0)
        pre = dummy

        for i in range(1, n+1):
            if i == m: pre_m = pre

            if i > m and i <= n:
                pre.next = head.next
                head.next = pre_m.next

                pre_m.next = head
                head = pre

            pre = head
            head = head.next

        return dummy.next

