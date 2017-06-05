class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class AddTwoNumbers(object):
    def addTwoNumbers(self, l1, l2):
        """
        :param l1:ListNode 
        :param l2:ListNode
        :return:ListNode 
        """
        dummy1, dummy2 = l1, l2
        head = dummy = ListNode(0)
        sum, carry = 0, 0
        while dummy1 or dummy2:
            if not dummy1:
                sum = dummy2.val + carry
                dummy2 = dummy2.next
            elif not dummy2:
                sum = dummy1.val + carry
                dummy1 = dummy1.next
            else:
                sum = dummy1.val + dummy2.val + carry
                dummy1, dummy2 = dummy1.next, dummy2.next
            carry = sum/10
            dummy.next = ListNode(sum%10)
            dummy = dummy.next
        if carry != 0:
            dummy.next = ListNode(carry)
        return head.next