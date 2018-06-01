# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        if head is None or head.next is None:
            return head
        dummyhead = ListNode(0)
        dummyhead.next = head

        p = dummyhead

        for i in range(m - 1):
            p = p.next

        curr = p.next
        for i in range(n - m):
            tmp = curr.next
            curr.next = tmp.next
            tmp.next = p.next
            p.next = tmp

        return dummyhead.next