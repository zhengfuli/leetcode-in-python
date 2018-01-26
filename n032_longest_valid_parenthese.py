class LongestValidParentheses(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        res, last = 0, -1
        for i in xrange(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif not stack:
                last = i
            else:
                stack.pop()
                if not stack:
                    res = max(res, i-last)
                else:
                    res = max(res, i-stack[len(stack)-1])
        return res