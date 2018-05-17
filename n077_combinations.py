class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ans = []

        stack = []

        x = 1

        while True:
            len_stack = len(stack)

            if len_stack == k:
                ans.append(stack[:])
            # backing when the length is met
            # or
            if len_stack == k or x > n - k + len_stack + 1:
                if not stack:
                    return ans
                x = stack.pop() + 1
            else:
                stack.append(x)
                x += 1
            print stack

if __name__ == '__main__':
    tb = Solution()
    tb.combine(3, 2)

