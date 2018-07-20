class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def digit_square_sum(n):
            sum = 0

            while n > 0:
                sum += int((n % 10) ** 2)
                n = int(n / 10)

            return sum

        slow, fast = n, digit_square_sum(n)
        while slow != fast:
            slow = digit_square_sum(slow)
            fast = digit_square_sum(fast)
            fast = digit_square_sum(fast)

            if slow == 1: return True

        return True if slow == 1 else False